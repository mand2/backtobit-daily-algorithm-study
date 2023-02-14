import sys;inp=sys.stdin.readline
j_money = s_money = int(inp().rstrip())  #j;준현, BNP / s:성민, 33
stock_price = list(map(int, inp().rstrip().split()))

# 준현
j_stock=0
for stock in stock_price:
    if j_money == 0: break
    if stock <= j_money:
        j_stock += j_money // stock
        j_money -= j_money // stock * stock
j_last_day = j_stock * stock_price[-1] + j_money

# 성민
# 전량 매수와 전량 매도
# 3일 연속 가격이 전일 대비 상승 => 매도  // 동일하다면 가격이 상승한 것이 아니다
# 3일 연속 가격이 전일 대비 하락 => 매수  // 동일하다면 가격이 상승한 것이 아니다

s_stock, up_cnt, down_cnt = 0, 0, 0
for i in range(1, 14):
    yesterday = stock_price[i-1]
    today = stock_price[i]

    if yesterday < today:
        up_cnt+=1
        down_cnt = 0 #초기화
        if up_cnt >= 3: # 3일 연속 가격이 전일 대비 상승 => 매도
            s_money += today * s_stock
            s_stock = 0

    if yesterday > today:
        down_cnt+=1
        up_cnt = 0
        if down_cnt >= 3: # 3일 연속 가격이 전일 대비 하락 => 매수
            s_stock += s_money // today
            s_money -= s_money // today * today

    if yesterday == today:
        up_cnt, down_cnt = 0, 0

s_last_day = (s_stock * stock_price[-1] + s_money)

print("BNP" if j_last_day > s_last_day else "TIMING" if j_last_day < s_last_day else "SAMESAME")


"""
첫 번째 줄에 준현이와 성민이에게 주어진 현금이 주어진다.
두 번째 줄에 2021년 1월 1일부터 2021년 1월 14일까지의 MachineDuck 주가가 공백을 두고 차례대로 주어진다.
모든 입력은 1000 이하의 양의 정수이다.
둘의 자산이 같다면 "SAMESAME"을 출력

100
10 20 23 34 55 30 22 19 12 45 23 44 34 38
성민이는 1월 8일에 5주를 매수한다. 따라서 1월 14일 195원의 자산을 가지게 된다.
    BNP
    
15
20 20 33 98 15 6 4 1 1 1 2 3 6 14
성민이는 1월 7일 3주를, 1월 8일 3주를 매수한다. 그리고 1월 13일에 전량 매도한다. 따라서 14일 자산은 36원이다.
    TIMING

"""

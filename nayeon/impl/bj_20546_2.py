money_jh = money_sm = int(input())
price = list(map(int, input().split()))
stock_jh = stock_sm = 0

# 준현의 BNP 전략
for p in price:
    if money_jh >= p:
        stock_jh += money_jh // p
        money_jh %= p   # 어차피 남은 값만 넣으면 되니까 %= 쓰는게 옳다..ㅎㅎ 까먹지말기

# 성민의 TIMING 전략
for i in range(3, len(price)):  # ""3일 연속"" 조건이라, 이렇게 빠르게 처리하면 좋을 듯!
    if price[i-3] > price[i-2] > price[i-1] > price[i]:
        stock_sm += money_sm // price[i]
        money_sm %= price[i]
    if price[i-3] < price[i-2] < price[i-1] < price[i]:
        money_sm += stock_sm * price[i]
        stock_sm = 0

assets_jh = money_jh + stock_jh * price[-1]
assets_sm = money_sm + stock_sm * price[-1]


## 여러줄
if assets_jh > assets_sm:
    print('BNP')
elif assets_jh == assets_sm:
    print('SAMESAME')
else:
    print('TIMING')

## 한줄
result = 'BNP' if assets_jh > assets_sm else 'SAMESAME' if assets_jh == assets_sm else 'TIMING'
print(result)

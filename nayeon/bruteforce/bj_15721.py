n = int(input())  # 전체사람
t = int(input())  # n회차
a = int(input())  # 0 뻔 / 1 데기

bundegi = []
bun = degi = 1  # 뻔/데기 자체 호출한 횟수
start = 0

# n 회차에 뻔 (n+3) / 데기 (n+3) 회 분다.

while True:
    prev = bun
    start+=1
    # for _ in range(start+3):  # 이렇게 한번에 퉁치면 횟수 체크 안됨. 순서대로 할 것.
    #     bundegi.append((bun, 0))
    #     bundegi.append((degi, 1))
    #     bun+=1
    #     degi+=1
    for _ in range(2):
        bundegi.append((bun, 0))
        bundegi.append((degi, 1))
        bun+=1
        degi+=1

    for _ in range(start+1):
        bundegi.append((bun, 0))
        bun+=1

    for _ in range(start+1):
        bundegi.append((degi, 1))
        degi+=1

    if prev < t <= bun:
        print(bundegi.index((t, a)) % n)  # 사람만큼 나누면 해당 위치의 사람이 나온다!
        break

"""
첫째 줄에 게임을 진행하는 사람 A명이 주어진다. (A ≤ 2000)
둘째 줄에는 구하고자 하는 번째 T가 주어진다. (T ≤ 10000)
셋째 줄에는 구하고자 하는 구호가 “뻔”이면 0, “데기”면 1로 주어진다.

즉 n-1회차 문장일 때는 ‘뻔 – 데기 – 뻔 – 데기 – 뻔(x n번) – 데기(x n번)’
일구가 0번째이고, 반시계 방향으로 게임 진행


8
2
0
    2
    
4
6
1
    3
"""

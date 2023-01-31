a, b = map(int, input().split())
cnt = 1
while True:
    if a == b: break
    elif a > b or (b % 10 != 1 and b % 2 != 0):
        cnt = -1
        break
    elif b % 2 == 0:
        b //= 2
        cnt += 1
    elif b % 10 == 1:
        b //= 10
        cnt += 1

print(cnt)
"""
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자. 만들 수 없는 경우에는 -1

2 162
    5 ( 2 4 8 81 162)

100 40021
    5 (100 → 200 → 2001 → 4002 → 40021)

4 42
    -1
"""

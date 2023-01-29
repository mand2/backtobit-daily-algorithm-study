import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
roads = list(map(int, inp().rstrip().split()))
price = list(map(int, inp().rstrip().split()))

min_price, cost = int(1e9), 0   # 제약조건: 리터당 가격은 1 이상 1,000,000,000 이하 고려해야함!

for i in range(n - 1):
    min_price = min(min_price, price[i])
    cost += min_price * roads[i]

print(cost)

"""
4
2 3 1
5 2 4 1
    18

4
3 3 4
1 1 1 1
    10

4
2 2 2
2 4 1 2
    10
"""

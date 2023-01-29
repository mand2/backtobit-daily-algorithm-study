import sys

inp = sys.stdin.readline
n = int(inp().rstrip())
customers = [int(inp().rstrip()) for _ in range(n)]
# customers.sort()   # 이렇게 하면 5 (1 1 1 1 2) = 1 로 나옴 ㅠ 2 로 나와야.
customers.sort(reverse=True)

print(sum([customers[i] - i for i in range(n) if customers[i] > i]))




"""
5
7
8
6
9
10
    30
5
1
1
1
1
2
    2
    
3
3
2
3
    5
    
4
3
3
3
3
    6
"""

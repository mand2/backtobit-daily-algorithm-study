# 34704kb	88ms
import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
c = [int(inp().rstrip()) for _ in range(n)]
c.sort(reverse=True)
print(sum(c) - sum(c[2::3]))

# print 부분 풀어서 쓴다고 하면 아래처럼.
# total = sum(c)
# free = sum(c[2::3])
# print(total - free)

"""
4
3
2
3
2
    8
---
6
6
4
5
5
5
5
    21
---
7
10
9
4
2
6
4
3
    29
"""

# 첫번째 문제풀이가 메모리 및 시간 덜 잡음.

import sys
sys.setrecursionlimit(10 ** 6)
inp = sys.stdin.readline
oup = sys.stdout.write

n = int(inp().rstrip())
graph = [list(map(int, inp().rstrip().split())) for _ in range(n)]

def pooling(size, x, y):
    if size == 2:
        tmp = [graph[x+0][y+0], graph[x+0][y+1], graph[x+1][y+0], graph[x+1][y+1]]
        tmp.sort()
        return tmp[2]
    size //= 2
    a1 = pooling(size, x, y)
    a2 = pooling(size, x+size, y)
    a3 = pooling(size, x, y+size)
    a4 = pooling(size, x+size, y+size)
    tmp = [a1, a2, a3, a4]
    tmp.sort()
    return tmp[2]

print(pooling(n, 0, 0))


"""
8
-1 2 14 7 4 -5 8 9
10 6 23 2 -1 -1 7 11
9 3 5 -2 4 4 6 6
7 15 0 8 21 20 6 6
19 8 12 -8 4 5 2 9
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
=> 17

4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4
=> 11
"""

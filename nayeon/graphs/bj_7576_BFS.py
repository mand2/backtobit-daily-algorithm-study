import sys
from collections import deque

inp = sys.stdin.readline

m, n = map(int, inp().rstrip().split())  # M(=y)은 상자의 가로 칸의 수, N(=x)은 상자의 세로 칸
graph = [list(map(int, inp().rstrip().split())) for _ in range(n)]

start_point = deque([(i, j) for i in range(n) for j in range(m) if graph[i][j] == 1])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while start_point:
    x, y = start_point.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            start_point.append((nx, ny))
            graph[nx][ny] = graph[x][y] + 1


res = 0
for g in graph:
    if 0 in g:
        res = 0
        break
    else:
        res = max(res, max(g))

print(res - 1)


"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
=> 8
"""

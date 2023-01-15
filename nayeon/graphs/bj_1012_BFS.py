import sys
from collections import deque

inp = sys.stdin.readline

CASE = int(inp().rstrip())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    graph[x][y] = 0
    q = deque([[x, y]])
    while q:
        w, h = q.popleft()
        for p in range(4):
            nx = w + dx[p]
            ny = h + dy[p]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])


while CASE > 0:
    CASE -= 1
    cnt = 0
    m, n, k = map(int, inp().rstrip().split())  # 1~50, 1~50, 1~2500
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, inp().rstrip().split())
        graph[a][b] = 1

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)

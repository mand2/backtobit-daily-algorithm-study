"""
N, M(2 ≤ N, M ≤ 100)
각각의 수들은 붙어서 입력
(0,0) -> (N-1, M-1)
"""

import sys

inp = sys.stdin.readline
from collections import deque

n, m = map(int, inp().rstrip().split())
graph = [list(map(int, inp().rstrip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([[0, 0]])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append([nx, ny])

print(graph[n-1][m-1])

"""
4 6
101111
101010
101011
111011
=> 15

4 6
110110
110110
111111
111101
=> 9

2 25
1011101110111011101110111
1110111011101110111011101
=> 38
"""

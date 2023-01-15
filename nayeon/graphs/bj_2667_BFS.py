import sys
from collections import deque

inp = sys.stdin.readline

# 남 북 동 서
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(inp().rstrip())  # 5 ~ 25
graph = [list(map(int, inp().rstrip())) for _ in range(N)]  # split() 하면 안됨. outOfIndex 나

cnt = 0  # 단지 수
houses = []  # 단지 내 집의 수


## bfs 실제 내부 코드
def bfs(x, y):
    graph[x][y] = 0  # 방문처리 ( == 처리 왜 ....ㅠㅠ 등호 표시 좀..)
    q = deque([[x, y]])
    c = 1
    while q:
        a, b = q.popleft()
        for r in range(4):
            nx = a + dx[r]
            ny = b + dy[r]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
                c += 1
                graph[nx][ny] = 0  # ( == 처리 왜 ....ㅠㅠ 등호 표시 좀..)
                q.append([nx, ny])
    houses.append(c)


for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)

houses.sort()
print(len(houses))
print(*houses, sep='\n')

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
7
8
9
"""

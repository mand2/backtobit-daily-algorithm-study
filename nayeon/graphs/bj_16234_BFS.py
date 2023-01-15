import sys
from collections import deque

inp = sys.stdin.readline

N, L, R = map(int, inp().rstrip().split())

graph = [list(map(int, inp().rstrip().split())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque([[x, y]])
    temp = [[x, y]]  # 국경이동 == 연합 리스트)

    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 \
                    and L <= abs(graph[nx][ny] - graph[a][b]) <= R:
                # `- graph[x][y]` 가 아님. 기준점은 큐에서 뽑아온 x,y 값
                visited[nx][ny] = 1
                q.append([nx, ny])
                temp.append([nx, ny])
    return temp

days = 0

while True:
    # visited = [[0] * N] * N  # 고정값을 정해준다.
    visited = [[0] * N for _ in range(N)]  # 루프 돌 때마다 선언
    flag = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                union = bfs(i, j)
                # 인구이동 시작
                if len(union) > 1:
                    flag = True
                    popular = sum([graph[x][y] for x, y in union]) // len(union)
                    for x, y in union:
                        graph[x][y] = popular

                # print(visited)
    if not flag:
        break

    days += 1

print(days)


"""
3 5 10
10 15 20
20 30 25
40 22 10
=> 2

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
=> 3
"""

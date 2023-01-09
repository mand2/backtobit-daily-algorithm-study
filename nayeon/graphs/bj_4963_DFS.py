import sys
sys.setrecursionlimit(10 ** 6)  # 런타임 방지 !! 필수 기본은 1,000 으로 매우 얕다.
inp = sys.stdin.readline


# 남 북 서 동 좌하 우상 우하 좌상
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def dfs(x, y):
    graph[x][y] = 0  # visited
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, inp().rstrip().split())
    graph = [list(map(int, inp().rstrip().split())) for _ in range(h)]
    if w == 0 and h == 0:
        break
    cnt = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)

"""
0, 1 중 1만 지나갈 수 있는 길.
연결 기준: 가로, 세로 또는 대각선으로 연결되어 있는 사각형

케이스
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0

출력
0
1
1
3
1
9
"""

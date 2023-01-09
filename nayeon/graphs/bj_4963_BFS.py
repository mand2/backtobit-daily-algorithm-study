import sys

inp = sys.stdin.readline

# 남 북 서 동 좌하 우상 우하 좌상  << x + 1 = 한 칸 아래로 , y + 1 = 한 칸 오른쪽
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def bfs(x, y):
    from collections import deque
    # 방문처리
    graph[x][y] = 0

    q = deque([[x, y]])
    while q:
        a, b = q.popleft()
        for k in range(8):  # 방향키 dx, dy 사이즈
            nx = a + dx[k]
            ny = b + dy[k]

            # validation: 그래프 안에 있는지 + 1의 값인지
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx, ny])


while True:  # 내부 함수 작성 후 적용할 것.
    w, h = map(int, inp().rstrip().split())
    # 0 0 으로 입력되지 않는 한 계속 테스트 케이스를 입력받는다
    if w == 0 and h == 0:
        break
    graph = [list(map(int, inp().rstrip().split())) for _ in range(h)]

    # visited = [] # 필요없음. 바로 방문처리함.
    cnt = 0

    # bfs 는 채워진다고 생각하고.. w , h 돌기
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)  # bfs.. 1 로 된 값을 채운다!
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

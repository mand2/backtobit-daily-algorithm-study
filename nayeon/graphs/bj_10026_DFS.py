import sys

sys.setrecursionlimit(10 ** 6)  # ** 이어야하는데 *로 씀. (실패원인 3)
inp = sys.stdin.readline

# DFS

N = int(inp())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

graph = [list(inp().rstrip()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]


def dfs(x, y):
    visit[x][y] = 1
    # color
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        # 급하게 복붙하느라 ^^ [ny][ny] 로 해놓고 안되고.. (실패원인 2)
        if (0 <= nx < N) and (0 <= ny < N) and visit[nx][ny] == 0:
            if graph[nx][ny] == graph[x][y]:
                dfs(nx, ny)


normal, weak = 0, 0  # 정상인 / 색약 구분구역

# normal
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            dfs(i, j)
            normal += 1

# weak
# 초기화 할 때 i, j 변수 왜 다 달라야 한다. 같으면... 에러... (실패원인 4)
# visit = [[0] * N] * N 절 대 안 됨 (실패원인 1)
visit = [[0] * N for _ in range(N)]

for a in range(N):
    for b in range(N):
        if graph[a][b] == 'G':
            graph[a][b] = 'R'

for c in range(N):
    for d in range(N):
        if visit[c][d] == 0:
            dfs(c, d)
            weak += 1

print(normal, weak)

"""
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
둘째 줄부터 N개 줄에는 그림이 주어진다.
R, G, B
크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑)
상하좌우로 인접

적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
=> 4 3
"""

"""
20
BBBBBRRRRRRRRRRRBBBB
BBBBBRRRRRRRRRRRBBBB
RBBBBBRRRRRRRRRRBBBB
RRRBBBBRRRRRRRRRBBBB
RRRBBBBRRRRRRRRRRBRB
GRRBBBBRRRRRRRRRRBRR
GGRRRRBBBRRRRRRRRBBB
GGGRRRBBBRRRRRRRRBBB
RRGGGGBBBRRRRRRRRBBB
BBGGGGBBBBRRRRRRRBBB
BBGGGGGBBBRRRRRRRBBB
GBGGGGGBRRRRRRRRRBBB
GGGGGGGGRRRRRRRRRBBB
GGGGGGGGGRRRRRRRRBBB
GGGGGGGGGGRRRRRRRBBB
RRGGGGGGGGGGRRRRRRBB
RRGGGGGGGGGGGGGGGRBB
RRRGGGGGGGGGGGGGGRBB
GGGGGGGBGGGGGGGGGGBB
RRRRGGGGGGGGGGGGGGGG

-> 11 6

5
GGGGG
GGGGG
GGGGG
GGGRB
GGGGG
=> 3 2

3
RRR
BBB
GGG
=> 3 3
"""

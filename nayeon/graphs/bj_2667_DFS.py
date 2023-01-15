import sys
sys.setrecursionlimit(10 ** 6)

inp = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(inp().rstrip())
graph = [list(map(int, inp().rstrip())) for _ in range(N)]

cnt = 0
houses = []

def dfs(x, y):
    graph[x][y] = 0
    global cnt  # 전역변수 선언
    cnt += 1
    for r in range(4):
        nx = x + dx[r]
        ny = y + dy[r]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1:
            dfs(nx, ny)

# houses = [dfs(i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            dfs(i, j)
            houses.append(cnt)
            cnt = 0



houses.sort()
print(len(houses))
print(*houses, sep='\n')

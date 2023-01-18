import sys

inp = sys.stdin.readline
from collections import deque

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, 1, -1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]

# m(가로y) n(세로x) h(높이)
m, n, h = map(int, inp().rstrip().split())

graph = [[list(map(int, inp().rstrip().split())) for _ in range(n)] for _ in range(h)]
start_point = deque([(i, j, k) for i in range(h) for j in range(n) for k in range(m) if graph[i][j][k] == 1])

while start_point:
    z, x, y = start_point.popleft()
    for vv in range(6):
        nx = x + dx[vv]
        ny = y + dy[vv]
        nz = z + dz[vv]
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h \
                and graph[nz][nx][ny] == 0:
            start_point.append((nz, nx, ny))
            graph[nz][nx][ny] = graph[z][x][y] + 1


"""
############## 이 방법도 맞긴 하지만, try-except-else 예외처리 해야 되어서 귀찮음
############## 메모리 좀 더 잡아먹고, 시간은 조금 짧으나.. 좀.. 가독성이...
res = 0
try:
    for g in graph:  # h
        for p in g:  # n
            for zz in p:  # m
                if zz == 0:
                    res = 0
                    # break (for 1개일 때만 가능)
                    raise Exception
            res = max(res, max(p))
except:
    print(res - 1)  # 처음부터 토마토가 익어있=0 // 모두 익지는 못하는 상황이면 -1 // 그 외 = 익기위한 시간 출력.
else:
    print(res - 1)  # 처음부터 토마토가 익어있=0 // 모두 익지는 못하는 상황이면 -1 // 그 외 = 익기위한 시간 출력.
"""

def getDay():
    res = 0
    for g in graph:  # h
        for p in g:  # n
            for zz in p:  # m
                if zz == 0:
                    return -1
            res = max(res, max(p))
    return res - 1


print(getDay())

"""
5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
=> 4

5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1
=> -1

4 3 2
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
-1 -1 -1 -1
1 1 1 -1
=> 0
"""

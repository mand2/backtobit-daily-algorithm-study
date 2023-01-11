from collections import deque
from sys import stdin
inp = stdin.readline  # 시간초과: readline 으로 변경하면 됨.

n, m = map(int, inp().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, inp().split())
    graph[a] += [b]
    graph[b] += [a]


def bfs(start):
    que = deque([start])
    visited[start] = True
    while que:
        curr = que.popleft()
        for k in graph[curr]:
            if not visited[k]:
                que.append(k)
                visited[k] = True


visited = [False] * (n + 1)
cnt = 0

for i in range(1, n + 1):
    if not visited[i]:  # 방문 전
        cnt += 1
        bfs(i)

print(cnt)

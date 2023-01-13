import sys
from collections import deque

inp = sys.stdin.readline

N = int(inp().rstrip())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, inp().rstrip().split())
    graph[a] += [b]
    graph[b] += [a]

q = deque()
q.append(1)

visited = [0] * (N + 1)

while q:
    curr = q.popleft()
    for i in graph[curr]:
        if visited[i] == 0:
            visited[i] = curr
            q.append(i)


print(*visited[2:], sep='\n')

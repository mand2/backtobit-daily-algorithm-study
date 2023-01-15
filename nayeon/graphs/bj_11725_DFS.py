import sys

sys.setrecursionlimit(10 ** 6)
inp = sys.stdin.readline

N = int(inp().rstrip())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, inp().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)
# visited[1] = 1

def dfs(root):
    for i in graph[root]:
        if visited[i] == 0:
            visited[i] = root
            dfs(i)

dfs(1)

for k in range(2, N + 1):
    print(visited[k])

"""
연결 요소를 Tree 로 변환해서 parent 를 찾는다.
"""

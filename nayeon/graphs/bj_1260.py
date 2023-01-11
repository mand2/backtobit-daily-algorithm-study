n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

for k in graph:
    k.sort()

## dfs
visited = []
def dfs(idx):
    visited.append(idx)
    for i in graph[idx]:
        if i not in visited:
            dfs(i)


dfs(v)
print(" ".join(map(str, visited)))

## bfs
from collections import deque

visited = [0] * (n + 1)
deq = deque([v])
visited[v] = 1
def bfs(idx):
    while deq:
        curr = deq.popleft()
        print(curr, end=" ")
        for i in graph[curr]:
            if visited[i] == 0:
                deq.append(i)
                visited[i] = 1

bfs(v)

"""
정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력

단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번
"""

"""
4 5 1           1 2 4 3
1 2             1 2 3 4
1 3             
1 4
2 4
3 4

5 5 3           3 1 2 5 4
5 4             3 1 4 2 5
5 2             
1 2
3 4
3 1
"""

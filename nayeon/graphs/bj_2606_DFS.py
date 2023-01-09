"""
30616	40
메모리kb / 시간ms
"""

N = int(input())
L = int(input())

graph = [[] for _ in range(N + 1)]
visited = []  # visit 배열을 정해놓고 하거나, 실제 방문한 곳만 넣는 방법 두 가지.
for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(idx):
    for i in graph[idx]:
        if i not in visited:
            visited.append(i)
            dfs(i)


dfs(1)
print(len(visited) - 1)

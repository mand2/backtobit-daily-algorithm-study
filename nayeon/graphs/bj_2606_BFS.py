"""
34104	72
메모리kb / 시간ms
"""

from collections import deque

#### 공통부분
N = int(input())  # 컴퓨터 수
L = int(input())  # 연결되어있는 개수

# (입력을 바로 받아오면 안됨 WHY? LS에 있는 모든 값을 방문하는 게 아님. 연결된 것만 방문.)
# > LS = [list(map(int, input().split())) for _ in range(L)]
# 초기화 먼저 필요.
graph = [[] for _ in range(N + 1)]  # [ [], [], [] ... [] ]
for _ in range(L):
    a, b = map(int, input().split())
    graph[a] += [b]  # 같은 위치에 또 추가가 될 수 있음. 덮어쓰는 것 아님
    graph[b] += [a]  # 같은 위치에 또 추가가 될 수 있음. 덮어쓰는 것 아님


###### sol.1 visit 배열을 정해놓고 하거나, 실제 방문한 곳만 넣는 방법 두 가지.
visited = [0] * (N + 1)
deq = deque([1])
visited[1] = 1

while deq:
    curr = deq.popleft()
    for i in graph[curr]:
        if visited[i] == 0:  # 처음 방문한 경우
            deq.append(i)
            visited[i] = 1
print(sum(visited) - 1)  # 1번 컴퓨터 제외


###### sol.2 visit 배열을 정해놓고 하거나, 실제 방문한 곳만 넣는 방법 두 가지.
visited = []
deq = deque([1])
while deq:
    curr = deq.popleft()
    for i in graph[curr]:
        if i not in visited:  # 처음 방문한 경우
            deq.append(i)
            visited.append(i)

print(len(visited) - 1)  # 1번 컴퓨터 제외

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7

=> 4
---
3
2
2 3
1 2

=> 2
"""

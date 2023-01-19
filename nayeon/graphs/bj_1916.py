import heapq
import sys

inp = sys.stdin.readline

INF = int(1e9)  # 우선순위 큐 _ 다익스트라

N = int(inp().rstrip())  # 도시개수-node
M = int(inp().rstrip())  # 버스개수-edge

graph = [[] for _ in range(N + 1)]
city = [INF] * (N + 1)  # 도시[i] 에 도착할 수 있는 최소 비용

for _ in range(M):
    a, b, c = map(int, inp().rstrip().split())
    graph[a] += [(c, b)]  # b: 목표, c:비용  => 즉 단방향.

start, end = map(int, inp().rstrip().split())


# 다익스트라
q = []
heapq.heappush(q, (0, start))  # heapq 에 넣을 때엔 (비용/거리/최소치...) , (노드번호) 순으로 넣어야 한다. 작은 거리= priority 높음.
city[start] = 0

while q:
    # dist, node = heapq.heappop(q)
    d, x = heapq.heappop(q)
    if city[x] < d:  # 최단거리가 아니면 pass
        continue

    for dd, xx in graph[x]:  # 연결된 다른 도시 탐색
        # nd, nx = cost , node
        nd = d + dd
        if nd < city[xx]:  # 인접 도시의 기존 값보다 nd 값이 더 싸다면 갱신
            heapq.heappush(q, (nd, xx))
            city[xx] = nd


print(city[end])

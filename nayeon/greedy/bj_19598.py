# [11000] 강의실 배정 과 문제 똑같음.

import sys
import heapq
inp = sys.stdin.readline
n = int(inp().rstrip())
m = [list(map(int, inp().rstrip().split())) for _ in range(n)]
m.sort()

room = []
heapq.heappush(room, m[0][1])
for s, e in m[1:]:
    if s < room[0]:
        heapq.heappush(room, e)
    else:
        heapq.heappop(room)
        heapq.heappush(room, e)

print(len(room))

"""
s < e, ei = s(i+1) 가능. 중간에 중단XX
N(1 ≤ N ≤ 100,000)

최소 회의실 개수를 출력

3
0 40
15 30
5 10
    2
    
2
10 20
5 10
    1
"""

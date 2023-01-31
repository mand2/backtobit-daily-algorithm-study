import heapq
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
times=[list(map(int, inp().rstrip().split())) for _ in range(n)]
# times.sort(key=lambda x: (x[1], x[0]))  # 이걸로 하면 4%에서 틀렸다고 나옴; 아마 heapq로 강의시작시간으로 검증하는 거라 sort()로 해야하는듯.

times.sort()
room=[]
heapq.heappush(room, times[0][1])

for s, e in times[1:]:
    if s < room[0]:  # 강의 시작시간이 현재 room의 끝나는 시간보다 빠르면 ..
        heapq.heappush(room, e)
    else:
        heapq.heappop(room)
        heapq.heappush(room, e)

print(len(room))
"""
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)
이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 10**9)
Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다

3
1 3
2 4
3 5
    2
    
4
1 3
2 3
2 4
3 5
    3
"""

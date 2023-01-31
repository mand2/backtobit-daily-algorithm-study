import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
meetings = [list(map(int, inp().rstrip().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))  # 끝시간을 먼저 정렬하는 경우, key에 튜플로 여러 인자를 주면 해당 인자의 순서대로 정렬!!

cnt = 1
end_time = meetings[0][1]
for s, e in meetings[1:]:  # range 설정 잘 할 것..
    if s >= end_time:
        cnt += 1
        end_time = e
print(cnt)

"""
첫번째: 회의의 개수
(1 4) => 시작시간 끝시간
끝남과 동시에 다른 회의 시작 가능, 시작=끝 도 가능.
시작 시간과 끝나는 시간은 (2**31)-1보다 작거나 같은 자연수 또는 0이다

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

=> 4
(1,4), (5,7), (8,11), (12,14) 를 이용

2
2 2
1 2
=> 2
"""

import sys
inp=sys.stdin.readline
n = int(inp().rstrip())
crane=sorted(list(map(int, inp().rstrip().split())), reverse=True)
m=int(inp().rstrip())
boxes=sorted(list(map(int, inp().rstrip().split())), reverse=True)

if crane[0] < boxes[0]:
    print(-1)
else:
    cnt = 0
    while boxes:
        for c in crane:
            if boxes and c < boxes[-1]:  # 이 조건이 없으면 무조건 시간초과 !!! O(n*m*k) = O(n**3) ...
                continue  # box는 있지만 현재 크레인이 가장 작은것도 못 들면 아래 for문 돌지말고 다시 cranefor문으로
            for b in boxes:
                if c >= b:
                    boxes.remove(b)
                    break

        cnt += 1
    print(cnt)
"""
3
6 8 9
5
2 5 2 4 7
    2
4
23 32 25 28
10
5 27 10 16 24 20 2 32 18 7
    3

10
11 17 5 2 20 7 5 5 20 7
5
18 18 15 15 17
    2
    
2
19 20
7
14 12 16 19 16 1 5
    4
"""

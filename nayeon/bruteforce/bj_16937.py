import sys;inp = sys.stdin.readline
h, w = map(int, inp().rstrip().split())
n = int(inp().rstrip())
stickers = [list(map(int, inp().rstrip().split())) for _ in range(n)]

# 문제풀이조건: 스티커를 그냥 있는 대로 다 받고 하나하나 검증한다. 처음 스티커 입력받을 때 검증하면 두개 조합할 때 복잡해짐.
result = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        r1, c1 = stickers[i]
        r2, c2 = stickers[j]
        area = r1 * c1 + r2 * c2

        if (r1+r2 <= h and max(c1,c2) <= w) \
                or (max(r1,r2) <= h and c1+c2 <= w):  # 정합
            result = max(result, area)

        elif (c1+r2 <= h and max(r1,c2) <= w) \
                or (max(c1,r2) <= h and r1+c2 <= w):  # 첫번째만 90도회전
            result = max(result, area)

        elif (r1+c2 <= h and max(c1,r2) <= w) \
                or (max(r1,c2) <= h and c1+r2 <= w):  # 두번째만 90도회전
            result = max(result, area)

        elif (c1+c2 <= h and max(r1,r2) <= w) \
                or (max(c1,c2) <= h and r1+r2 <= w):  # 모두 90도회전
            result = max(result, area)
print(result)



"""
1 ≤ H, W, N ≤ 100
1 ≤ Ri, Ci ≤ 100
첫째 줄에 모눈종이의 크기 H, W, 둘째 줄에 스티커의 수 N이 주어진다. 다음 N개의 줄에는 스티커의 크기 Ri, Ci가 주어진다
그 중 2개만 뽑는다. 최대 면적을 구한다.

2 2
2
1 2
2 1
    4
    - 1*2 + 1*2 
    - 2*1 + 2*1

10 9
4
2 3
1 1
5 10
9 11
    56
    
1 3
2
1 1
1 1
    2
"""

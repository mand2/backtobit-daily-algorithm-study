import sys
from itertools import combinations

inp=sys.stdin.readline
n,m=map(int, inp().rstrip().split())
arr=[list(map(int, inp().rstrip().split())) for _ in range(n)] # 인당 선호하는 치킨 각각 나눠서 받아온다~
result=0

# 간략버전
for i1, i2, i3 in combinations(range(m), 3):
    result=max(result, sum([max(arr[k][i1], arr[k][i2], arr[k][i3]) for k in range(n)]))
print(result)



# 이해하기 쉬운 수식 버전
result=0
for i1, i2, i3 in combinations(range(m), 3):  # 0 1 2 3 4, 즉 치킨 번호 조합 만든다. == 행렬의 가로(=[][요기..!])의 조합을 찾는다.
    # 각 조합 (i1, i2, i3)의 값으로 회원당 최대 선호도 값 찾기!
    temp=[max(arr[k][i1], arr[k][i2], arr[k][i3]) for k in range(n)]   # 회원당 최대 선호도 값
    result = max(sum(temp), result)  # 회원별 최대선호도의 합 과 기존 result값 비교
print(result)

"""
!!!! 한 사람의 만족도는 시킨 치킨 중에서 선호도가 가장 큰 값으로 결정 !!!!
첫 번째 줄에 고리 회원의 수 N (1 ≤ N ≤ 30) 과 치킨 종류의 수 M (3 ≤ M ≤ 30) 이 주어집니다.
두 번째 줄부터 N개의 줄에 각 회원의 치킨 선호도가 주어집니다.
i+1번째 줄에는 i번째 회원의 선호도 ai,1, ai,2, ..., ai,M (1 ≤ ai,j ≤ 9) 가 주어집니다.

첫 번째 줄에 고리 회원들의 만족도의 합의 최댓값을 출력합니다.

3 5
1 2 3 4 5
5 4 3 2 1
1 2 3 2 1

    13
-->
    회원번호 \ 치킨(1 ~ 5) 에 대한 선호도
    회원번호1: 1 2 3 4 5
    회원번호2: 5 4 3 2 1 
    회원번호3: 1 2 3 2 1
    치킨 5, 1, 3 번을 뽑아야 만족도 13이 된다.
    
4 6
1 2 3 4 5 6
6 5 4 3 2 1
3 2 7 9 2 5
4 5 6 3 2 1
    25
"""

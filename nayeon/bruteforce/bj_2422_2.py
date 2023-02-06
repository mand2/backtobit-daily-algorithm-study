# 안될 조합만 받지 말고, 전체 리스트에서 안되는 bad 값 세팅하기
# 메모리, 시간, 코드 길이 모두 월등함 메모리 1/4 씀ㅋ
import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
bad = [[0] * (n+1) for _ in range(n+1)]  # n*n
result = 0
for _ in range(m):
    a, b = map(int, inp().rstrip().split())
    bad[a][b]=bad[b][a] = 1

for k1 in range(1, n-1):
    for k2 in range(k1+1, n):
        for k3 in range(k2+1, n+1):
            if bad[k1][k2] or bad[k1][k3] or bad[k2][k3]:
                continue
            result += 1

print(result)


"""
(1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000)

최악조합의 경우를 피하면서 아이스크림을 3가지 선택
선택하는 방법이 몇 가지인지 구하려고 한다.

5 3
1 2
3 4
1 3
    3
"""

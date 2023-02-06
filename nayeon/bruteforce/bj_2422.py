from itertools import combinations  # 조합 nCx
import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
# 안될 조합만 받지 말고, 전체 리스트에서 안되는 bad 값 세팅하기
# bad = sorted(list(map(int, inp().rstrip().split())) for _ in range(m))

bad = [[0] * (n+1) for _ in range(n+1)]  # n*n
num = [_ for _ in range(1, n+1)]
result = 0
for _ in range(m):
    a, b = map(int, inp().rstrip().split())
    bad[a][b] = 1
    bad[b][a] = 1

for k in list(combinations(num, 3)):  # combination 돌지 않고 for문 3개 돌려도 됨. 메모리적게잡아먹음.
    if bad[k[0]][k[1]] or bad[k[0]][k[2]] or bad[k[1]][k[2]]:
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

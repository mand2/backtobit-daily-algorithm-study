import sys
inp = sys.stdin.readline

n, k = map(int, inp().rstrip().split())
coins = [int(inp().rstrip()) for _ in range(n)]
cnt = 0

for i in range(1, n+1):
    cnt += k // coins[-i]
    k = k % coins[-i]

print(cnt)

"""
첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
    (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) => "Ai는 Ai-1의 배수" 조건 때문에 그리디 가능.

10 4200
1
5
10
50
100
500
1000
5000
10000
50000
    6

10 4790
1
5
10
50
100
500
1000
5000
10000
50000
    12
"""

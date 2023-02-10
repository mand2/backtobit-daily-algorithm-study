import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
dp = [0] * (n + 1)  # dp[n+1] = n일째.  dp=받는 값.
for i in range(1, n + 1):
    t, p = map(int, inp().rstrip().split())
    dp[i] = max(dp[i], dp[i - 1])  # n일째 값과 (n-1)째 값 비교 // dp[1] ~ dp[n] 까지 넣어줌.
    if i + t < n + 2:  # 일자비교. n+2 == 퇴사일(n+1)의 인덱스값. dp 의 인덱스값으로 봐야한다.
        dp[i + t - 1] = max(dp[i - 1] + p, dp[i + t - 1])  # 상담끝나는 날짜의 dp 값 업데이트..! (j+t-1) 흐흐..
print(dp[-1])

"""
 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담

첫째 줄에 N (1 ≤ N ≤ 15)이 주어진다.
둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
    45
"""

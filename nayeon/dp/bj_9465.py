case = int(input())
for _ in range(case):
    line = int(input())
    dp = [list(map(int, input().split())) for _ in range(2)]

    if line > 1:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
        for i in range(2, line):
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][line - 1], dp[1][line - 1]))

"""
# [0,1] 을 떼어낸다고 할 때 사용할 수 없는 위치들
x o x
? x ?

# [1,3]
? ? ? x ?
? ? x o x

2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80

260, 290
"""

N = int(input())

# 풀이 1 시간 112
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, N + 1):
    if i == 2:
        dp[2] = 2
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N] % 10007)


# 풀이 2 시간 116
dp = [1, 2]
if N < 3:
    print(N)
else:
    for i in range(N-2):
        dp.append(dp[-1] + dp[-2])
    print(dp[-1] % 10007)

"""
1 -> 1 (1)
2 -> 1+1 2 (2)
3 -> 1+1+1 1+2 2+1 (3)
4 -> (5)
    1 1 1 1
    1 1 2
    1 2 1
    2 1 1
    2 2
5 ->
    1 1 1 1 1
    1 1 1 2
    1 1 2 1
    1 2 1 1
    2 1 1 1
    2 2 1
    1 2 2
    2 1 2

1 2 3 5 8 13 21 34 55
"""

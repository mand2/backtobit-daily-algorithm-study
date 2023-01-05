N = int(input())

# 풀이 1
if N == 1:
    print(1)
elif N == 2:
    print(3)
else:
    dp = [0] * (N + 1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    print(dp[N] % 10007)

# 풀이 2
dp = [0, 1, 3]
for i in range(3, N + 1):
    dp.append(dp[i - 1] + dp[i - 2] * 2)
print(dp[N] % 10007)

"""
2×n(높*가) 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

1 -> 1
2 -> (1*2)*2  (2*1)*2  2*2
3 -> (1)+2*2 (2)
"""

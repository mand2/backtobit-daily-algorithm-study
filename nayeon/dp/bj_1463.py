N = int(input())

# bottom up
dp = [0] * (1 + N)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])

# top down
dp = {1: 0}


def calc(n):
    if n in dp.keys():
        return dp[n]
    if (n % 3 == 0) and (n % 2 == 0):
        dp[n] = min(calc(n // 3) + 1, calc(n // 2) + 1)
    elif n % 3 == 0:
        dp[n] = min(calc(n // 3) + 1, calc(n - 1) + 1)
    elif n % 2 == 0:
        dp[n] = min(calc(n // 2) + 1, calc(n - 1) + 1)
    else:
        dp[n] = calc(n - 1) + 1
    return dp[n]


print(calc(N))

"""
그리디 알고리즘은 내가 생각한 처음 최적의 방법이 끝까지 반례 없이 적용이 되는 경우에 이용하고,
동적 계획법은 가능성을 모두 두고 그 안에 최솟값을 찾을 수 있다

DP: bottom-up / top-down 두 방식이 있음.
"""

"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

{1: 0, 2: 1, 3: 1, 4: 2, 5: 3, 6: 2, 7: 3, 8: 3, 9: 2, 10: 3}
2 -> /2 (1)
3 -> /3 (1)
4 -> /2, /2 (2)
5 -> -1, _4 (3)
6 -> /3 /2 (2)
7 -> -1 _6 (3)
8 -> /2 /2 /2 (3)
9 -> /3 /3 (2)
"""

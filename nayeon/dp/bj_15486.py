from sys import stdin

N = int(stdin.readline())


# (생각의흐름1) 상담이 끝나고 난 후, 실제 임금 지급일에 수익을 저장..
nums = [0] * (51 + N)
for i in range(1, N + 1):
    a, b = map(int, stdin.readline().split())
    nums[i + a] = max(b, nums[i + a])

print(sum(nums[:N + 2]))

### (생각의흐름2)
# 처음부터 받을 수 있는 값만 저장하도록 dp 설정. (nums 배열 자른 느낌?)
# 이렇게 하면 N+1 에 생기는 값이 없을 수도 있음. 오류 수정필요!
dp = [0] * (N + 2)

for i in range(1, N + 1):
    a, b = map(int, stdin.readline().split())
    dp[i] = max(dp[i - 1], dp[i])
    if i + a < N + 2:
        dp[i + a] = max(dp[i] + b, dp[i + a])

print(dp[-1])


# 실제 제출 코드 (생각의흐름3 : 2번 수정)
dp = [0] * (N + 1)

for i in range(1, N + 1):
    a, b = map(int, stdin.readline().split())
    dp[i] = max(dp[i - 1], dp[i])
    if i + a < N + 2:
        dp[i + a - 1] = max(dp[i - 1] + b, dp[i + a - 1])  # 해당 일자에 미리 값이 들어간 경우가 있을 수 있으므로 max 로 걸러주기

print(dp[-1])


# 실제 제출 코드 (생각의흐름4 : 2번 흐름을 원하는 방향으로 세팅한 답!)
dp = [0] * (N + 1)

for i in range(N):
    a, b = map(int, stdin.readline().split())
    dp[i + 1] = max(dp[i + 1], dp[i])
    if i + a < N + 1:
        dp[i + a] = max(dp[i] + b, dp[i + a])

print(dp[-1])

"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
=> 45

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
=> 55

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
=> 20

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
=> 90
"""

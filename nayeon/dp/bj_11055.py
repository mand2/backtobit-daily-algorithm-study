# 풀이 1 : 해당 값을 다 포함 (= 현재까지 sum 하기)
input()
dp = [0] * 1001
for i in map(int, input().split()):
    dp[i] = max(dp[:i]) + i

print(max(dp))

# 풀이 2
N = int(input())
nums = list(map(int, input().split()))
dp = [0] * N
dp[0] = nums[0]
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        else:  # else 있어야 함. why? sum 한 값을 다 보여줘야 함.. dp 배열 내부에
            dp[i] = max(dp[i], nums[i])
print(max(dp))

"""
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 2, 50, 60} 이고, 합은 113이다.

10 {1 100 2 50 60 3 5 6 7 8} = 113
4 {2 6 3 4} = 9
3 {10 10 10} = 10

##########
# default
idx   0 1 2 3
nums  2 6 3 4
dp    2 0 0 0

# i = 1 , j = 0
idx   0 1 2 3
nums  2 6 3 4
dp    2 8 0 0

# i = 2 , j = 0
idx   0 1 2 3
nums  2 6 3 4
dp    2 8 5 0

# i = 2 , j = 1 (X)

# i = 3 , j = 0
idx   0 1 2 3
nums  2 6 3 4
dp    2 8 5 6

# i = 3 , j = 1 (X)
# i = 3 , j = 2
idx   0 1 2 3
nums  2 6 3 4
dp    2 8 5 9

"""

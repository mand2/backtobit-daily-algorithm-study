# 망할 다 시간초과 뜸 >>   pyp3 으로하면 통과 ㅋ 근데 시간 오래걸림

n = int(input())
arr=[0]*(n+1)  # 0 ... n+1 까지  # 미리 할당하고 다시 읽어들이면 시간초과.
arr[1]=1
# bf
for i in range(2,n+1):
    j = 1
    min_v = 4
    while((j**2)<=i):
        a = arr[i-(j**2)]
        min_v = min(min_v,a)
        j+=1
    arr[i] = min_v+1
print(arr[n])



# dp
import math
n = int(input())
dp = [0,1]
for i in range(2, n+1):
    minValue = 4
    for j in range(1, int(math.sqrt(i)) + 1):
        minValue = min(minValue, dp[i - j**2])
    dp.append(minValue + 1)

print(dp[n])

"""
여기서, 1 ≤ n ≤ 50,000이다.
모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현

규칙: n - (n보다 작거나 같은 제곱수) 를 인덱스로 갖는 값에 +=1


#######
문제 풀이 : DP 문제로 풀이 할 수 있다. 자신의 수에서 그보다 작은 수의 제곱수를 뺀 것의 최소를 구하고 거기에 한개를 더해주면 된다.
가능한 다른 풀이 : 브루트포스로 가능한 모든 경우를 풀어 볼 수도 있다.

 


25 => 1
26 => 2
11339 = 105**2 + 15**2 + 8**2 + 5**2. (4)
"""

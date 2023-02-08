# 1 2 3 4 값이 나올 수 있다

import sys
k = int(sys.stdin.readline().rstrip())

def square(n):
    if (n**0.5).is_integer():
        return 1  # 제곱수면 1
    for i in range(1, int(n ** 0.5) + 1):  # n보다 작은 범위의 제곱수의 원본값
        if n < i ** 2:
            break
        if ((n - i ** 2) ** 0.5).is_integer():
            return 2
    for i in range(1, int(n**0.5) + 1):
        if n < i ** 2:
            break
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if n < i ** 2 + j ** 2:
                break
            if ((n - i ** 2 - j ** 2) ** 0.5).is_integer():
                return 3
    return 4

print(square(k))

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

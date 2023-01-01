n = list(map(int, input().split()))


# 풀이 1 , 18초
# print(n[0] + n[1])
# print(n[0] - n[1])
# print(n[0] * n[1])
# print(n[0] // n[1])
# print(n[0] % n[1])
# print('%.2f' % (n[0] / n[1]))

# 풀이 2 , 16초
def call():
    return [
        n[0] + n[1],
        n[0] - n[1],
        n[0] * n[1],
        n[0] // n[1],
        n[0] % n[1],
        '%.2f' % (n[0] / n[1])
    ]


print(*call(), sep='\n')

"""
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
단, b는 0이 아니다.

정수 2개가 공백을 두고 입력된다.
"""

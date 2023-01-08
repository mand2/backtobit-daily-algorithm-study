a = ord(input())

for i in range(a - 97 + 1):
    print(chr(i + 97))  # 이렇게 해도 맞긴 맞음
    print(chr(i + 97), end=' ')  # 이게 정석.


start = ord('a')
while start <= a:
    print(chr(start), end=' ')
    start += 1


"""
[기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)

영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.
"""

a, b, c = map(int, input().split())

k = a if a < b else b  # 가장 작은 값
print(k if k < c else c)

# print(min(a, b, c))  3항 쓰지 않을 때.
"""
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.
"""

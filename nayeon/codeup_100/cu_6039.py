from sys import stdin

n = list(map(float, stdin.readline().rstrip().split()))
# n = list(map(float, input().split()))  # 위에 쓰는 것과 별 차이가 없음. 짧아서 그런 듯.
print((n[0] ** n[1]))


"""
실수 2개(f1, f2)를 입력받아
f1을 f2번 거듭제곱한 값을 출력하는 프로그램을 작성해보자.
 
2개의 실수(f1, f2)가 공백으로 구분되어 입력된다.
"""

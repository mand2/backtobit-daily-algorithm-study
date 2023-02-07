import sys
from itertools import product

n, k = map(int, input().split())
len_max = len(str(n))

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort(reverse=True)
flag = 1

while flag:
    prod = list(product(numbers, repeat=len_max))
    for i in prod:
        temp = ''.join(map(str,i))
        if n >= int(temp):
            print(temp)
            flag = 0
            break

    len_max -= 1

"""
첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.
(10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3)
각 원소는 1부터 9까지의 자연수

657 3
1 5 7 
    577

반례)
100000000 1
1
Ans : 11111111 (9자리가 아닌 8자리)

1000 1
1
    111

15 2
9 9
    9
"""

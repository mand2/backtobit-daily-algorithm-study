n = int(input())
drinks = list(map(int, input().split()))
drinks.sort()

print('%g' % ((sum(drinks[:-1]) / 2) + drinks[n - 1]))  # 정수일 땐 정수로, 실수일 땐 실수로.

"""
10 9 6 3 2
    10+4.5 6 3 2
14.5 6 3 2
    14.5+3 3 2
17.5 3 2
    17.5+1.5 2
19 2
    19+1
20
--
2 3 5 9 10
    1+3 5 9 10
4 5 9 10
    2+5 9 10
7 9 10
    3.5+9 10
12.5 10
    6.25 10
16.25
"""

""""
5
3 2 10 9 6
    20

10
100 9 77 65 39 27 45 1 80 495
    716.5
"""

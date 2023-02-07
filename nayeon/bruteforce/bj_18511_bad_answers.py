# 첫번째 시도
# 반례가 계속 있음
# result=''
# if (int(n) % 10) == 0:
#     n = str(int(n)-1)
#
# for num in n:
#     temp = [i for i in arr if i <= num]
#     result += max(temp)
# print(result)

# 두번째 시도 ㅠ
# from itertools import product
# import sys
# inp = sys.stdin.readline
# n, k = map(int, inp().rstrip().split())
# arr = list(map(int, inp().rstrip().split()))
# l = len(str(n))
#
# while True:
#     temp = list(product(arr, repeat=l))  # repeat을 통해 몇개를 뽑을지 설정한다.= 중복조합
#     ex = []
#     for i in temp:
#         now=int(''.join(i))
#         if now <= n:
#             ex.append(now)
#     if len(ex) >= 1:
#         print(max(ex))
#         break
#     else:
#         l -= 1

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

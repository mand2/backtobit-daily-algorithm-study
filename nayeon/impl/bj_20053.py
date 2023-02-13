import sys;inp=sys.stdin.readline
tc=int(inp().rstrip())
for _ in range(tc):
    num=int(inp().rstrip())
    n_list=list(map(int, inp().rstrip().split()))
    print(min(n_list), max(n_list))


# short-coding
for _ in range(int(inp().rstrip())):
    int(inp().rstrip())
    arr = list(map(int, inp().rstrip().split()))
    print(min(arr), max(arr))

"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 10)가 주어진다.
각 테스트 케이스는 두 줄로 이루어져 있다.

각 테스트 케이스의 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.

모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.


3
5
20 28 22 25 21
5
30 21 17 25 29
5
20 10 35 30 7

    20 28
    17 30
    7 35
"""

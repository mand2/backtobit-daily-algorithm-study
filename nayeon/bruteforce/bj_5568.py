import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
k = int(inp().rstrip())
nums = [int(inp().rstrip()) for _ in range(n)]

s1 = set()

from itertools import permutations  # 순서가 있는..조합   combinations XX
for a in permutations(nums, k):
    s1.add(''.join(map(str, a)))

print(len(s1))
"""
첫째 줄에 n이, 둘째 줄에 k가 주어진다. 셋째 줄부터 n개 줄에는 카드에 적혀있는 수가 주어진다.
상근이가 만들 수 있는 정수의 개수를 출력한다.

n (4 ≤ n ≤ 10)
k (2 ≤ k ≤ 4)
각 카드의 숫자 : (1 ≤  ≤ 99)

4
2
1
2
12
1
    7

6
3
72
2
12
7
2
1
    68
"""


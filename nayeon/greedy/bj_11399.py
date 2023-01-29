import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
p = list(map(int, inp().rstrip().split()))
p.sort()
print(sum([p[i] * (n-i) for i in range(n)]))

"""
print 부분 풀어서 쓴다고 하면 아래처럼.
s = [p[i] * (n-i) for i in range(n)]
print(sum(s))
"""

"""
첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)

    줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어졌을 때, 
    각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

5
3 1 4 3 2
    => 32
"""

from sys import stdin

n = int(stdin.readline().rstrip())


def solution(k):
    if k < 2:
        return k
    return solution(k - 1) + solution(k - 2)


print(solution(n))

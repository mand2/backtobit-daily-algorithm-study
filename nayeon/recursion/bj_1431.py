from sys import stdin

n = int(stdin.readline().rstrip())
nums = list(stdin.readline().rstrip() for _ in range(n))


# 숫자만 더한다
def sum_nums(x):
    s = 0
    for i in x:
        if i.isdigit():
            s += int(i)
    return s


# sorting 조건. 첫번째가 같다 -> 두번째 -> 세번째.
nums.sort(key=lambda x: (len(x), sum_nums(x), x))

print(*nums, sep='\n')

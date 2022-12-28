from sys import stdin

n = int(stdin.readline().rstrip())
nums = list(stdin.readline().rstrip() for _ in range(n))


# 숫자만 더한다
def sum_nums(x):
    s = 0
    for i in x:
        s += 1 if i.isdigit() else 0
    return s


nums.sort(key=lambda x: (len(x), sum_nums(x), x))

print(*nums, sep='\n')

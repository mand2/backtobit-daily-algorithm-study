from sys import stdin

N = int(stdin.readline().rstrip())
nums = list(int(stdin.readline().rstrip()) for _ in range(N))

nums.sort()

print(*nums, sep='\n')

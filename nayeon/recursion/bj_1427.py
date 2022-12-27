from sys import stdin

n = list(stdin.readline().rstrip())
n.sort(reverse=True)
print("".join(map(str, n)))

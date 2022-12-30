import sys

# sys.setrecursionlimit(10 ** 6) << 메모리초과됨.

def append_star(num):
    if num == 1:
        return ['*']

    stars = append_star(num // 3)
    group = []

    for star in stars:
        group.append(star * 3)
    for star in stars:
        group.append(star + ' ' * (num // 3) + star)
    for star in stars:
        group.append(star * 3)
    return group


n = int(sys.stdin.readline().strip())
print(*append_star(n), sep='\n')

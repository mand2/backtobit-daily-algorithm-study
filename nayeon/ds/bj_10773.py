from sys import stdin

r = []


def p():
    return int(stdin.readline().strip())


for _ in range(p()):
    v = p()
    r.append(v) if v > 0 else r.pop()

print(sum(r))

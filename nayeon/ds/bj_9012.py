from sys import stdin

inp = stdin.readline


def check(vps):
    c = 0
    for i in vps:
        if c < 0: return False
        c += 1 if i == '(' else -1
    return c == 0


for _ in range(int(inp().rstrip())):
    vps = inp().rstrip()
    print('YES') if check(vps) else print('NO')

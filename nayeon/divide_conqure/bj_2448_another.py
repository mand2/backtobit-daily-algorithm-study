"""
숏코딩에서 참고할만한.
"""

n = int(input())


def draw(size):
    if size == 3:
        return ['  *  ', ' * * ', '*****']

    inner = draw(size // 2)
    s = []
    for i in inner:
        s.append(' ' * (size // 2) + i + ' ' * (size // 2))
    for i in inner:
        s.append(i + ' ' + i)

    return s


print(*draw(n), sep='\n')

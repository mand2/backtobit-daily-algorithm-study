n, r, c = map(int, input().split())

# https://ggasoon2.tistory.com/11
def sol(size, x, y):
    if size == 0:
        return 0

    # return 2 * (x % 2) + (y % 2) + 4 * sol(size - 1, int(x / 2), int(y / 2))
    return 2 * (x % 2) + (y % 2) + 4 * sol(size - 1, x//2, y//2)


print(sol(n, r, c))

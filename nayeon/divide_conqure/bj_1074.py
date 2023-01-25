n, r, c = map(int, input().split())
cnt = 0

while n > 1:
    size = 2 ** (n - 1)
    partial = size ** 2  # (2^(n-1))^2 = 4^(n-1)
    if r < size and c < size:  # 2사분면
        cnt += partial * 0
    elif r < size and c >= size:  # 1사분면
        cnt += partial * 1
        c -= size
    elif r >= size and c < size:  # 3사분면
        cnt += partial * 2
        r -= size
    elif r >= size and c >= size:  # 4사분면
        cnt += partial * 3
        r -= size
        c -= size
    n -= 1

if r == 0 and c == 0:
    print(cnt)
if r == 0 and c == 1:
    print(cnt + 1)
if r == 1 and c == 0:
    print(cnt + 2)
if r == 1 and c == 1:
    print(cnt + 3)

### n = 3
# def test3(x, y, k):
#     p = 2 ** k  # 8
#     t = p // 2
# test2(x+0, y+0, p*0)
# test2(x+0, y+t, p*1)
# test2(x+t, y+0, p*2)
# test2(x+t, y+t, p*3)


"""
n => (4 ** n) 개의 칸
r행 c열을 몇 번째로 방문했는지

1 ≤ N ≤ 15
0 ≤ r, c < 2**N


0   1   4    5
2   3   6    7
8   9   12   13
10  11  14   15


2 3 1 -> 11
3 7 7 -> 63

10 511 511
    262143

10 512 512
    786432



"""

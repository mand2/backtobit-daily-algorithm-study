import sys;inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
bulb = list(map(int, inp().rstrip().split()))

for _ in range(m):
    a, l, r = map(int, inp().rstrip().split())
    if a == 1:  # i 번째 전구의 상태를 x로 변경한다.
        bulb[l - 1] = r
    elif a == 2:  # l부터 r번째까지 전구의 상태를 변경한다.
        for b in range(l-1, r):
            if bulb[b] == 0:
                bulb[b] = 1
            else:
                bulb[b] = 0
    elif a == 3:  # l부터 r번째까지 전구를 끈다
        for b in range(l-1, r):
            bulb[b] = 0
    elif a == 4:  # l부터 r번째까지 전구를 킨다.
        for b in range(l-1, r):
            bulb[b] = 1
print(*bulb)


"""
1 ≤ N, M ≤ 4,000
1 ≤ a ≤ 4
0 ≤ s, x ≤ 1
1 ≤ l ≤ r ≤ N
1 ≤ i ≤ N


8 3
0 0 0 0 0 0 0 0
1 2 1
1 4 1
2 2 4

    0 0 1 0 0 0 0 0

8 3
0 0 0 0 0 0 0 0
1 2 1
1 4 1
3 2 4
"""

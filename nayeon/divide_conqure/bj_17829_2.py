import sys
sys.setrecursionlimit(10 ** 6)
inp = sys.stdin.readline

n = int(inp().rstrip())
graph = [list(map(int, inp().rstrip().split())) for _ in range(n)]


def pooling(size, list):
    ng = [[] for _ in range(size // 2)]
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            tmp = [list[i + 0][j + 0], list[i + 0][j + 1], list[i + 1][j + 0], list[i + 1][j + 1]]
            tmp.sort()
            ng[i // 2].append(tmp[-2])

    print(ng[0][0]) if size == 2 else pooling(size//2, ng)

pooling(n, graph)


"""
8
-1 2 14 7 4 -5 8 9
10 6 23 2 -1 -1 7 11
9 3 5 -2 4 4 6 6
7 15 0 8 21 20 6 6
19 8 12 -8 4 5 2 9
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
=> 17

4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4
=> 11
"""

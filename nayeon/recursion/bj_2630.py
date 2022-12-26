from sys import stdin

N = int(stdin.readline())
MAP = [list(map(int, stdin.readline().split())) for _ in range(N)]

result = [0, 0]


def solution(x, y, n):
    color = MAP[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != MAP[i][j]:
                # recursion (n은 2의 제곱수라, // 쓰지 않아도 되는 게 아님. 정수값이 나와야 함)
                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return

    if color == 0:
        result[0] += 1
    else:
        result[1] += 1


solution(0, 0, N)
print(result[0])  # 하얀색 0
print(result[1])  # 파란색 1

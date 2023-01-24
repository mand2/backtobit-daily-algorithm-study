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

"""
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 
색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.
"""

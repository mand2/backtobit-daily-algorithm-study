import sys
sys.setrecursionlimit(10 ** 6)
inp = sys.stdin.readline
oup = sys.stdout.write

n = int(inp())
graph = [list(inp()) for _ in range(n)]
res = []

def recur(x, y, z):
    color = graph[x][y]
    flag = False
    for i in range(x, x + z):
        if set(graph[i][y:y + z]) != set(color):
            flag = True
    if not flag:
        res.append(color)
        return

    z //= 2
    res.append('(')
    recur(x, y, z)
    recur(x, y + z, z)
    recur(x + z, y, z)
    recur(x + z, y + z, z)
    res.append(')')


recur(0, 0, n)
# print(*res, sep='')
oup("".join(map(str, res)))

"""
흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다.
흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면,
쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다.
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고,
왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며,
이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다


숫자 N 이 주어진다. N 은 언제나 2의 제곱수로 주어지며, 1 ≤ N ≤ 64의 범위를 가진다. 두 번째 줄부터는 길이 N의 문자열이 N개 들어온다.
"""

"""
8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111


(0(0011)(0(0111)01)1)


입력 

8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
=> 
((110(0101))(0010)1(0001))
"""

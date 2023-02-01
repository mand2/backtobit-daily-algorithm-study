import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
k = int(inp().rstrip())
g = sorted(list(map(int, inp().rstrip().split())))

bar = [g[i + 1] - g[i] for i in range(n - 1)]
print(sum(sorted(bar)[:n-k]))


"""
고속도로는 평면상의 직선이라고 가정
단, 집중국의 수신 가능영역의 길이는 0 이상이며 모든 센서의 좌표가 다를 필요는 없다.

첫째 줄에 센서의 개수 N(1 ≤ N ≤ 10,000),
둘째 줄에 집중국의 개수 K(1 ≤ K ≤ 1000)가 주어진다.
셋째 줄에는 N개의 센서의 좌표가 한 개의 정수로 N개 주어진다. 각 좌표 사이에는 빈 칸이 하나 있으며, 좌표의 절댓값은 1,000,000 이하이다.

6
2
1 6 9 3 6 7
    5
    
10
5
20 3 14 6 7 8 18 10 12 15
    7


"""

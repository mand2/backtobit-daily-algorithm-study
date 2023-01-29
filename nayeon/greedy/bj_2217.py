# ( w의 값은 고정된다. 즉, w1 과 w2을 섞어서 쓰는 게 아님)
# 38112 KB 	96 MS
import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
rope = [int(inp().rstrip()) for _ in range(n)]
rope.sort(reverse=True)
print(max([rope[i] * (i + 1) for i in range(n)]))

"""
N(1 ≤ N ≤ 100,000)개의 로프
모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.
    k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, ( w의 값은 고정된다. 즉, w1 과 w2을 섞어서 쓰는 게 아님)
    각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.


첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.
2
10
15
=> 20

5
5
4
2
2
2
=> 10
"""

import sys;inp=sys.stdin.readline
cows=[-1]*11
cnt=[0]*11
n=int(inp().rstrip())
for _ in range(n):
    idx, position = map(int, inp().rstrip().split())
    if cows[idx+1] == -1:
        cows[idx+1] = position
    if cows[idx+1] != position:
        cows[idx+1] = position
        cnt[idx+1] += 1

print(min(c for c in cnt if c > 0))  # 1 이 나옴 ..흠..
print(sum(cnt))  # 3 나오는데 런타임;


"""
존이 할 일은 소가 길을 건너는 것을 관찰하는 것이다.
존은 소의 위치를 N번 관찰하는데,
각 관찰은 소의 번호와 소의 위치 하나씩으로 이루어져 있다.
존은 소를 10마리 가지고 있으므로 소의 번호는 1 이상 10 이하의 정수고,
소의 위치는 길의 왼쪽과 오른쪽을 의미하는 0과 1 중 하나다.

이 관찰 기록을 가지고 소가 최소 몇 번 길을 건넜는지 알아보자. 즉 같은 번호의 소가 위치를 바꾼 것이 몇 번인지 세면 된다.



첫 줄에 관찰 횟수 N이 주어진다.
1 ≤ N ≤ 100 정수
다음 N줄에는 한 줄에 하나씩 관찰 결과가 주어진다.
관찰 결과는 소의 번호와 위치(0 또는 1)로 이루어져 있다.

첫 줄에 소가 길을 건너간 최소 횟수를 출력한다.
소 번호 1 ≤  ≤ 10

8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1

3
"""

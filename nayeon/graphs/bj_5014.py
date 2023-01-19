from collections import deque

f, s, g, u, d = map(int, input().split())
building = [0] * 1_000_0000

df = [u, -d]

q = deque([s])  # 현재 위치 세팅
building[s] = 1


if s == g:
    print(0)
else:
    while q:
        x = q.popleft()
        if g == x:
            break
        for i in range(2):
            nf = df[i] + x
            if 0 < nf <= f and building[nf] == 0:
                building[nf] = building[x] + 1
                q.append(nf)
    if building[g] == 0:
        print('use the stairs')
    else:
        print(building[g] - 1)  # 0 층은 없다. ground floor XXXX!!!
"""
F = 총 건물 층 수
G = 면접장 층
S = 강호가 있는 곳
1 <= <= 1,000,000
U D : 0 <= <= 1,000,000

G층에 갈 수 없다면, "use the stairs"를 출력한다.

10 1 10 2 1 
=> 6

100 2 1 1 0
=> use the stairs
"""

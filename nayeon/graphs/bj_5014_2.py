f, s, g, u, d = map(int, input().split())
building = [1] * (f + 1)  # 1 = 미방문으로 세팅
cnt = 0

checklist = [s]  # 방문해야할 리스트
flag = 1
building[s] = 0

while checklist and flag:
    temp = []
    for c in checklist:
        if c == g:
            flag = 0
        if c + u <= f and building[c + u]:
            building[c + u] = 0
            temp += [c + u]
        if c - d > 0 and building[c - d]:
            building[c - d] = 0
            temp += [c - d]
    checklist = temp[:]  # tmp 배열 자체를 checklist로 반환.
    cnt += 1

if flag:
    print('use the stairs')
else:
    print(cnt - 1)

"""
이 코드는 다른 분 코드를 참고해서 작성.
내 코드의 1/4 정도를 메모리로 쓴다..WOW
"""

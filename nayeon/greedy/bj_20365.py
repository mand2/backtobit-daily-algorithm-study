n = int(input())
graph = input() # list(input()) 안해도 됨ㅋ string 이니까

color = {'B': 0, 'R': 0}
color[graph[0]] += 1  # default 시작값
for i in range(1, n):
    if graph[i] != graph[i-1]:
        color[graph[i]] += 1

print(1 + min(color['B'], color['R']))

"""
문제의 수 N (1 ≤ N ≤ 500,000)
둘째 줄에 N개의 문자가 공백 없이 순서대로
R은 빨간색, B는 파란색

8
BBRBRBBR
    4
"""

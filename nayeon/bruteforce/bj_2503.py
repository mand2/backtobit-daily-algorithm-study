import sys
from itertools import permutations  # 123 != 321 이므로 순열 필요
inp = sys.stdin.readline
n = int(inp().rstrip())
# questions = [list(map(int, inp().rstrip().split())) for _ in range(n)]  # 이렇게 하는 것보다 받아올 때마다 체크하고 지우는 게 더 나음
# possible = list(permutations(range(1, 10), 3))  # 숫자라서 하나하나 체크하는거 귀찮음.

items=['1','2','3','4','5','6','7','8','9']
possible = list(permutations(items, 3))

for _ in range(n):
    question, s, b = map(int, inp().rstrip().split())
    rmv_cnt=0  # 이게 있는 이유: list 에서 remove 해주면 idx 전체가 다 바뀜. 으휴~~~
    for idx in range(len(possible)):
        idx -= rmv_cnt
        strike=ball=0
        temp=str(question)
        for i in range(3):
            if temp[i] == possible[idx][i]:
                strike+=1
            elif possible[idx][i] in temp:
                ball+=1
        if (s!=strike) or (b!=ball):
            possible.remove(possible[idx])
            rmv_cnt+=1

print(len(possible))

"""
첫째 줄에는 민혁이가 영수에게 몇 번이나 질문을 했는지를 나타내는 1 이상 100 이하의 자연수 N이 주어진다. 
이어지는 N개의 줄에는 각 줄마다 민혁이가 질문한 세 자리 수와 
    영수가 답한 스트라이크 개수를 나타내는 정수와 
    볼의 개수를 나타내는 정수, 
이렇게 총 세 개의 정수가 빈칸을 사이에 두고 주어진다.

A: 1에서 9까지의 서로 다른 숫자 세 개
Q: 1에서 9까지의 서로 다른 숫자 세 개

4
123 1 1
356 1 0
327 2 0
489 0 1
    2
"""

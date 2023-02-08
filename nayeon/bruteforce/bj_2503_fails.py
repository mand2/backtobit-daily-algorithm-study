import sys
from itertools import permutations  # 123 != 321 이므로 순열 필요
inp = sys.stdin.readline
n = int(inp().rstrip())

items=['1','2','3','4','5','6','7','8','9']
possible = list(permutations(items, 3))

# for _ in range(n):
    # question, s, b = map(int, inp().rstrip().split())
    # for p in possible:  # p:str
    #     strike=ball=0
    #     temp=str(question)  #tmp: str, question:int
    #     # 회당 질문한 값과 possible 값을 비교
    #     for i in range(3):
    #         if temp[i]==p[i]:
    #             strike+=1
    #         elif p[i] in temp:
    #             ball+=1
    #     if (s!=strike) or (b!=ball):
    #         possible.remove(p)  # ('1', '2', '4'), ('1', '2', '6'), ('1', '2', '8'), 로 제대로 삭제가 안되는 상황.
    # print('---', len(possible), possible)


# 실패
for _ in range(n):
    question, s, b = map(int, inp().rstrip().split())
    for p in possible:  # p:str
        strike=ball=0
        temp=str(question)  #tmp: str, question:int
        # 회당 질문한 값과 possible 값을 비교
        for i in range(3):
            if temp[i]==p[i]:
                strike+=1
            elif p[i] in temp:
                ball+=1
        if (s!=strike) or (b!=ball):
            possible.remove(p)  # ('1', '2', '4'), ('1', '2', '6'), ('1', '2', '8'), 로 제대로 삭제가 안되는 상황.

print(len(possible))

# 얘도 실패.
t_p = possible
for _ in range(n):
    question, s, b = map(int, inp().rstrip().split())
    for p in possible:  # p:str
        strike=ball=0
        temp=str(question)  #tmp: str, question:int
        # 회당 질문한 값과 possible 값을 비교
        for i in range(3):
            if temp[i]==p[i]:
                strike+=1
            elif p[i] in temp:
                ball+=1
        if (s!=strike) or (b!=ball):
            t_p.remove(p)

    possible=t_p
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

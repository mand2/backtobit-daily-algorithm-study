i = int(input())

while i > 0:
    i -= 1
    print(i)

print('------------------')

for j in range(i, -1, -1):
    print(j)

"""
[기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2

정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.
1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.

입력 5
=> {4 3 2 1 0}

"""

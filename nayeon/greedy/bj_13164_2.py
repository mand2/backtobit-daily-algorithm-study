# 기존 값 좀 더 짧게 구문 바꿔서..! 시간 50 ms 나 줄음.
n, group = map(int, input().split())
kids = list(map(int, input().split()))

bar = [kids[i+1] - kids[i] for i in range(n-1)]
bar.sort()
print(sum(bar[:n-group]))


"""
n 명이 있으면 경계는 (n-1)개
그룹 group 개수로 묶는다면, (group-1)의 경계가 있어야 한다.


"""

"""
이렇게 나뉘어진 조들은 각자 단체 티셔츠를 맞추려고 한다. 
조마다 티셔츠를 맞추는 비용은 조에서 가장 키가 큰 원생과 가장 키가 작은 원생의 키 차이만큼 든다. 
K개의 조에 대해 티셔츠 만드는 비용의 합을 최소로 하고 싶어한다. 태양이를 도와 최소의 비용을 구하자.

5 3
1 3 5 6 10
(1 3) (5 6) (10) => 2 + 1 + 0
 (2) 2 (1) 4
    3
    
8 4
1 2 3 5 6 8 11 16
(1 2 3) (5 6 8) (11) (16) 
 (1 1) 2 (1 2) 3 5
    => 5    
"""
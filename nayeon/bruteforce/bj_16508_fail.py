# 맞긴 맞았지만 시간초과로 실패 ! => 문자열간 비교를 t 기준으로 해야된다.
# book의 문자열은 최대 50, t는 10이기 때문. + 쓸데없는 tmp_dic 이 있어서 시간초과 ㅋ
import sys;inp = sys.stdin.readline

t = inp().rstrip()
n = int(inp().rstrip())
book = sorted(list(inp().rstrip().split()) for _ in range(n))

# 단어가 알파벳 몇개씩 할당되었는지 체크
dic = [0] * 26
for word in t:
    dic[ord(word) - 65] += 1  # ord('A') = 65


"""
# 망했던 풀이 중 하나. 아래에서 tmp_dic = dic 으로 하면 A값의 변화가 B로 공유됨..
price = 0
for b in book:  # 이거는 모든 조합에 대한 체크가 아님..
    p = int(b[0])
    for b_word in b[1]:
        dic[ord(b_word) - 65] -= 1  # 각 단어를 빼준다!
    price += p
    # 다 채웠으면 끝!
    if max(dic) < 1:
        print('끄으으응', price)
        break

print(-1) if max(dic)>0 else print(price)
"""

price_list=[]
for i in range(1 << len(book)):  # 1개 ~ n개 뽑을 때의 각조합의 총 개수는 비트연산으로 쌉가능.. 와우내
    mix_word, mix_price= '', 0
    tmp_dic = [0] * 26
    for word in t:
        tmp_dic[ord(word) - 65] += 1  # ord('A') = 65

    for j in range(len(book)):
        # 이제 실제 조합을 해준다
        if i & (1 << j):
            mix_word += book[j][1]  # 조합에 들어갈 모든 문자열을 다 더해준다.
            mix_price += int(book[j][0])  # 조합에 들어갈 전공책 값을 다 더해준다.

    for b_word in mix_word:
        tmp_dic[ord(b_word) - 65] -= 1
        if max(tmp_dic) < 1:
            price_list.append(mix_price)
            continue

print(-1) if len(price_list)==0 else print(min(price_list))


"""
첫 번째 줄에는 민호가 만들고자 하는 단어를 의미하는 문자열 T (1 ≤ |T| ≤ 10)가 주어진다. T는 항상 대문자이며, |T|는 문자열 T의 길이를 의미한다.
두 번째 줄에는 민호가 가진 전공책의 개수를 의미하는 정수 N (1 ≤ N ≤ 16)이 주어진다.
다음 N개의 각 줄에는 전공책 가격을 의미하는 정수 Ci (10,000 ≤ Ci ≤ 100,000)와 제목을 의미하는 문자열 Wi (1 ≤ |Wi| ≤ 50)가 주어진다. Wi는 항상 대문자이다.
"""


"""
예제
ANT
4
35000 COMPUTERARCHITECTURE
47000 ALGORITHM
43000 NETWORK
40000 OPERATINGSYSTEM
    40000

ALMIGHTY
4
35000 COMPUTERARCHITECTURE
47000 ALGORITHM
43000 NETWORK
40000 OPERATINGSYSTEM
    87000

BAKEJOON
3
25000 JAVA
10000 OOP
30000 BINARYCHECK
    65000

JAVA
2
30000 CPLUSPLUS
25000 PYTHON
    -1
"""

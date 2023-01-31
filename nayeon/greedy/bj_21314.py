mknum = input()

m = 0
min = max = ''  # 동시할당

## 문자열 돌면서 K 가 있을 때
#   max: 그동안의 MMMK 들의 값 을 다 찾음 // min: 그 앞의 MMM 따로, K따로 구해주기
for num in mknum:
    if num == 'M':
        m += 1
    else:
        min += str(5) if m == 0 else str(10 ** m + 5)  # 0 인 경우 체크하는 게 까다로웠음
        max += str(10 ** m * 5)
        m = 0  # 다시 초기화

if m > 0:
    min += str(10 ** (m - 1))
    max += '1' * m

print(max, min, sep='\n')

"""
주어진 민겸 수가 십진수로 변환되었을 때 가질 수 있는 값 중
가장 큰 값과 가장 작은 값을 두 줄로 나누어 출력한다.

정수 N에 대해 10N 또는 5 × 10N 꼴의 십진수를 대문자 M과 K로 이루어진 문자열로 표기
10**N 꼴의 십진수는 N + 1개의 M으로,   MMM...
5 × 10**N 꼴의 십진수는 N개의 M 뒤에 1개의 K를 이어붙인 문자열 (MM...)K


MKKMMK
    505500
    155105

MKM
    501
    151
"""

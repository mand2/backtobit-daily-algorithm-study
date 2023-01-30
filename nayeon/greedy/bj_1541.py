"""
- 로 나누고,
    그 문자열을 + 기준으로 나눈 후, + 범주에 있는 애들끼리는 더해준다.
- 범주에 있는 값들을 다 뺄셈처리.
"""

num = input().split('-')
result = []

for n in num:
    a = sum(int(_) for _ in n.split('+'))
    result.append(a)

print(result[0] - sum(result[1:]))

"""
55-50+40
  50 - (50+40)
    = -35
    
10+20+30+40
    100

00009-00009
    0
"""

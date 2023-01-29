p = input()
p = p.replace('XXXX', 'AAAA').replace('XX', 'BB')
print(-1) if 'X' in p else print(p)

# print([p,-1]['X' in p])  => [p, -1] 의 배열 중 ('X' in p) 인 값에 따라 반환한다. True=1임..

"""
XXXXXX
    AAAABB
XX.XX
    BB.BB
XXXX....XXX.....XX
    -1
X
    -1
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX
    BB.AAAAAAAABB..AAAAAAAA...AAAABB
"""

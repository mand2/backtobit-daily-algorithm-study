# 기존 버전 업데이트

import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
arr = [list(inp().rstrip()) for _ in range(n)]
cnt = 0
result = ''
for i in range(m): # 열
    dna = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(n): # 행
        dna[arr[j][i]] += 1
    # max_v = [k for k, v in dna.items() if max(dna.values()) == v][0]
    max_v = max(dna, key=dna.get)  # dna.get() 안됨!
    result += max_v
    cnt += sum(dna.values()) - dna[max_v]

print(result)
print(cnt)

"""
A T G C
1: DNA의 수 N과 문자열의 길이 M
    N≤1000 , M≤50
2~(N+1) DNA

Hamming Distance의 합이 가장 작은 DNA 를 출력하고,
둘째 줄에는 그 Hamming Distance의 합

DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력: A C G T



5 8
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT
    TAAGATAC
    7
    
4 10
ACGTACGTAC
CCGTACGTAG
GCGTACGTAT
TCGTACGTAA
    ACGTACGTAA
    6

6 10
ATGTTACCAT
AAGTTACGAT
AACAAAGCAA
AAGTTACCTT
AAGTTACCAA
TACTTACCAA
    AAGTTACCAA
    12
"""

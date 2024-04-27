import sys;inp=sys.stdin.readline

plate = [list(map(int, inp().rstrip().split())) for _ in range(5)]
call_nums = [list(map(int, inp().rstrip().split())) for _ in range(5)]

print(plate, sep='\n')
print(call_nums, sep='\n')




"""
1~5 : 나의 빙고판
6~10 : 사회자가 빙고 번호를 불러준다.


11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15

    15
"""

import sys

n = int(sys.stdin.readline().rstrip())

cnt = n // 5

if n == 1 or n == 3:
    cnt = -1
elif (n % 5) % 2 == 0:
    cnt += (n % 5) // 2
else:
    cnt = (n // 5) - 1
    cnt += (n - (cnt * 5)) // 2

print(cnt)


"""
첫째 줄에 거스름돈 액수 n(1 ≤ n ≤ 100,000)이 주어진다.
2 / 5 원 무한.
거스름돈 동전의 최소 개수를 출력한다. 만약 거슬러 줄 수 없으면 -1을 출력한다.


0 1 2 3 4 5 6 7 8 9
=> 1 3 의 나머지는 안됨.  
"""

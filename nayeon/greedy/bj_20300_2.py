n = int(input())
loss = list(map(int, input().split()))
loss.sort()
m, a = (0, n) if n % 2 == 0 else (loss[-1], n - 1)
for i in range(a // 2):
    m = max(loss[i] + loss[a - 1 - i], m)
print(m)

"""
5
1 2 3 4 5
    5
    
4
1 7 8 9
    15
"""

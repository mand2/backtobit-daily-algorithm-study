n = int(input())
loss = list(map(int, input().split()))
loss.sort()
flag = 0 if n % 2 == 0 else 1

m = 0
if flag:
    m = loss[-1]
    for i in range((n-1)//2):
        m = max(loss[i] + loss[-2-i], m)
else:
    for i in range((n)//2):
        m = max(loss[i] + loss[-1-i], m)
print(m)

"""
5
1 2 3 4 5
    5
    
4
1 7 8 9
    15
"""

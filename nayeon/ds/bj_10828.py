from sys import stdin
from collections import deque

deq = deque()

for _ in range(int(stdin.readline())):
    order = stdin.readline().split()
    if order[0] == 'push':
        deq.append(order[1])
    elif order[0] == 'top':
        print('-1') if len(deq) == 0 else print(deq[len(deq) - 1])
    elif order[0] == 'pop':
        print('-1') if len(deq) == 0 else print(deq.pop())
    elif order[0] == 'size':
        print(len(deq))
    else:
        print('1') if len(deq) == 0 else print('0')

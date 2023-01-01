from sys import stdin

num = int(stdin.readline().rstrip())
print(2 ** num - 1)


def hanoi(step, start, to, by):
    if step == 1:
        print(start, to)
    else:
        hanoi(step - 1, start, by, to)
        # print(333333, to, start)
        print(start, to)
        hanoi(step - 1, by, to, start)


hanoi(num, 1, 3, 2)

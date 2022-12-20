from sys import stdin

# A = 65 /
# chr => 아스키를 char로 / ord => char => ascii

n = int(stdin.readline().rstrip())
state = stdin.readline().rstrip()
nums = [0] * n

for i in range(n):
    nums[i] = int(stdin.readline().rstrip())

stack = []


def calculate(operator, first, second):
    if operator == '+':
        return first + second
    if operator == '-':
        return first - second
    if operator == '*':
        return first * second
    if operator == '/':
        return first / second


for w in state:
    if 'A' <= w <= 'Z':
        stack.append(nums[ord(w)-65])
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(calculate(w, b, a))

print('%.2f' % stack.pop())

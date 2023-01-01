woods = list(map(int, input().split()))


def check():
    for i in range(4):
        if woods[i] > woods[i + 1]:
            ref = woods[i + 1]
            woods[i + 1] = woods[i]
            woods[i] = ref
            print(*woods)
    if [1, 2, 3, 4, 5] != woods:
        check()


check()

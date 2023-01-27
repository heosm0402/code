# https://www.acmicpc.net/problem/1107
import itertools


N = int(input())
M = int(input())

fullButtons = [i for i in range(10)]
if M != 0:
    wrongButtons = list(map(int, input().split()))
    buttonList = list(set(fullButtons)-set(wrongButtons))

    minimum = abs(N - 100)
    for i in range(len(str(N)) + 1):
        p = itertools.product(buttonList, repeat=i + 1)

        for target in p:
            num = 0
            for idx, e in enumerate(target[::-1]):
                num += (10 ** idx) * e

            buttonCount = len(str(num)) + abs(N - num)
            # print(num, buttonCount)
            minimum = min(minimum, buttonCount)

    print(minimum)
else:
    print(min(len(str(N)), abs(N-100)))

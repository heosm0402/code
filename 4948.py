# https://www.acmicpc.net/problem/4948
import sys


while 1:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break

    numberList = [0, 0] + [1] * (2*n-1)
    primeList = []
    for idx in range(len(numberList)):
        if not numberList[idx]:
            continue
        if n < idx <= 2*n:
            primeList.append(idx)
        for removeIdx in range(idx, len(numberList), idx):
            numberList[removeIdx] = 0

    print(len(primeList))

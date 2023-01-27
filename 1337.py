# https://www.acmicpc.net/problem/1337
import sys


def checkNearElem(target):
    checkList = [
        range(target-4, target+1),
        range(target-3, target+2),
        range(target-2, target+3),
        range(target-1, target+4),
        range(target-0, target+5),
    ]

    moreNeed = 100
    for checkRange in checkList:
        tempMoreNeed = 0
        for checkNumber in checkRange:
            if checkNumber not in l:
                tempMoreNeed += 1

        moreNeed = min(moreNeed, tempMoreNeed)

    return moreNeed


N = int(sys.stdin.readline().rstrip())
l = []
for _ in range(N):
    l.append(int(sys.stdin.readline().rstrip()))

l.sort()
answer = 100
for elem in l:
    tempAnswer = checkNearElem(elem)
    answer = min(answer, tempAnswer)
    if answer == 0:
        break

print(answer)

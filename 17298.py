import sys

n = int(input())
numList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
answer = []
while numList:
    num = numList.pop(0)
    elseList = [i for i in numList if i > num]
    if elseList:
        answer.append(elseList[0])
    else:
        answer.append(-1)

print(" ".join(map(str, answer)))

# https://www.acmicpc.net/problem/1244
import sys


switchNumber = int(input())
switchList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
N = int(sys.stdin.readline().rstrip())


for idx in range(N):
    sex, number = map(int, sys.stdin.readline().rstrip().split(" "))
    # print("!", sex, number)
    if sex == 1:
        loop_n = 1
        while 1:
            try:
                switchList[(number * loop_n)-1] += 1
                loop_n += 1
            except:
                break
    else:
        loop_n = 1
        while 1:
            checkLeftIdx, checkRightIdx = number-1-loop_n, number-1+loop_n
            if checkLeftIdx < 0 or checkRightIdx >= switchNumber:
                break

            if (switchList[checkLeftIdx] % 2) == (switchList[checkRightIdx] % 2):
                loop_n += 1
            else:
                break

        for add_one in range(checkLeftIdx+1, checkRightIdx):
            switchList[add_one] += 1

# print(switchList)
for idx, item in enumerate(switchList):
    if (idx + 1) == 0:
        print(item % 2, end=' ')
    elif (idx + 1) == len(switchList):
        print(item % 2)
    elif (idx + 1) % 20 == 0:
        print(item % 2)
    else:
        print(item % 2, end=' ')

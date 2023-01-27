# https://www.acmicpc.net/problem/1072
import sys

X, Y = map(int, sys.stdin.readline().rstrip().split(" "))
Z = int(Y / X * 100)
if Z >= 99:
    print(-1)
    exit(0)

minMoreGame = 10e9
maxMoreGame = X
moreGame = X // 2
isFindMax = False
isFindMin = False
while 1:
    newZ = int((Y+moreGame) / (X+moreGame) * 100)
    if newZ == Z+1:
        maxMoreGame = moreGame
        isFindMax = True

    if newZ == Z:
        minMoreGame = moreGame
        isFindMin = True

    if isFindMin and isFindMax:
        break
    else:
        moreGame = moreGame // 2


for i in range(minMoreGame, maxMoreGame+1):
    newZ = int((Y + i) / (X + i) * 100)
    if newZ != Z:
        print(i)
        break

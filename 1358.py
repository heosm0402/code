# https://www.acmicpc.net/problem/1358
import math
import sys

W, H, X, Y, P = map(int, sys.stdin.readline().rstrip().split(" "))


def isInside(playerX, playerY):
    global W
    global H
    global X
    global Y
    radiance = int(H/2)
    leftCircleX, leftCircleY = X, Y + radiance
    rightCircleX, rightCircleY = X + W, Y + radiance
    # print("LL", leftCircleX, leftCircleY)
    # print("RR", rightCircleX, rightCircleY)
    # print(math.sqrt(abs(playerX-leftCircleX) + abs(playerY-leftCircleY)) ** 2)
    if math.sqrt(abs(playerX-leftCircleX) ** 2 + abs(playerY-leftCircleY) ** 2) <= radiance:
        # print("@", math.sqrt(abs(playerX-leftCircleX) ** 2 + abs(playerY-leftCircleY) ** 2))
        return 1
    elif math.sqrt(abs(playerX-rightCircleX) ** 2 + abs(playerY-rightCircleY) ** 2) <= radiance:
        # print("#", math.sqrt(abs(playerX-rightCircleX) ** 2 + abs(playerY-rightCircleY) ** 2))
        return 1
    elif (X <= playerX <= X + W) and (Y <= playerY <= Y + H):
        # print("$", X, playerX, X+W, "$", Y, playerY, Y+H)
        return 1
    else:
        return 0


cnt = 0
for _ in range(P):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    result = isInside(x, y)
    # print("!", x, y, result)
    cnt += result

print(cnt)

# https://www.acmicpc.net/problem/1697
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split(" "))
distList = [0] * (100000 + 1)

toCheck = deque()
toCheck.append(N)

while toCheck:
    position = toCheck.popleft()
    if position == K:
        print(distList[position])
        exit(0)

    for newPosition in [position-1, position+1, position*2]:
        if (0 <= newPosition <= 100000) and not distList[newPosition]:
            distList[newPosition] = distList[position] + 1
            toCheck.append(newPosition)

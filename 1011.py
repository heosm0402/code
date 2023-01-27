# https://www.acmicpc.net/problem/1011
import sys
from collections import deque


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    distance = y - x

    n = 1
    while 1:
        if distance <= n * (n+1):
            break
        else:
            n += 1

    if distance <= n ** 2:
        print((n*2)-1)
    else:
        print(n*2)

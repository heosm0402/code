# https://www.acmicpc.net/problem/2529
from collections import deque

k = int(input())
l = list(input().split())


def backTracking():
    if len(l) == 0:
        print("".join(r))
        return





l = deque(list(range(0, 10)))
r = list()
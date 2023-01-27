# https://www.acmicpc.net/problem/1655

from collections import deque
N = int(input())

q = deque()
for _ in range(N):
    t = int(input())
    q.append(t)


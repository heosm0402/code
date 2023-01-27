# https://www.acmicpc.net/problem/2151
import sys
from collections import deque
# up left down rigth
delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

input = sys.stdin.readline
N = int(input())


def bfs(start, graph):
    q = deque()
    q.append(start)

    while q:
        y, x = q.popleft()

        for idx in 4:
            nx = x + delta[idx]
            ny = y + delta[idx]

            if not 0 <= nx < N or not 0 <= ny < N:
                continue



    return graph


room = []
for _ in range(N):
    room.append(list(input().rstrip()))

for y in range(N):
    for x in range(N):
        if room[y][x] == "#":
            result = bfs((y, x), room)

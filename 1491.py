# https://www.acmicpc.net/problem/1491
import sys
from collections import deque


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
graph = [[0 for i in range(N)] for j in range(M)]

q = deque()
q.append((0, 0))
delta = [(-1, 0), (0, -1), (1, 0), (0, 1)] # up left down right
direction = 3

while q:
    print(q)
    y, x = q.pop()
    graph[y][x] = 1
    ny = y + delta[direction][0]
    nx = x + delta[direction][1]

    allVisit = True
    for i in range(4):
        if 0 <= x+delta[i][1] < N and 0 <= y+delta[i][0] < M:
            if graph[y+delta[i][0]][x+delta[i][1]] == 0:
                allVisit = False

    if allVisit:
        break

    if (not (0 <= nx < N and 0 <= ny < M)) or graph[ny][nx] == 1:
        direction = (direction - 1) % 4
        q.append((y+delta[direction][0], x+delta[direction][1]))
    else:
        q.append((ny, nx))


print(x, y)

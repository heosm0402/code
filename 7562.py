# https://www.acmicpc.net/problem/7562
import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

delta = [(-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2)]

for _ in range(N):
    length = int(sys.stdin.readline().rstrip())
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    t_x, t_y = map(int, sys.stdin.readline().rstrip().split(" "))
    if x == t_x and y == t_y:
        print(0)
        continue

    visited = [[0 for i in range(length)] for j in range(length)]
    q = deque()
    q.append((x, y))

    while q:
        isFind = False
        x, y = q.popleft()
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if ny == t_y and nx == t_x:
                isFind = True
                print(visited[y][x] + 1)
                break

            if 0 <= nx < length and 0 <= ny < length:
                if not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx, ny))

        if isFind:
            break

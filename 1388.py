# https://www.acmicpc.net/problem/1388
import sys
from collections import deque

# up down left right
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]

def dfs(start):
    global w
    global h
    global graph

    isVisited[start[0]][start[1]] = 1
    q = deque()
    q.append(start)

    while q:
        y, x = q.pop()

        if graph[y][x] == "-":
            dy = [0, 0]
            dx = [-1, 1]
        else:
            dy = [-1, 1]
            dx = [0, 0]

        for idx in range(2):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if not ((0 <= ny < h) and (0 <= nx < w)):
                continue

            if isVisited[ny][nx]:
                continue

            if graph[y][x] == graph[ny][nx]:
                isVisited[ny][nx] = 1
                q.append((ny, nx))


h, w = map(int, sys.stdin.readline().rstrip().split(" "))

isVisited = [[0 for i in range(w)] for j in range(h)]
graph = []
for _ in range(h):
    graph.append(list(sys.stdin.readline().rstrip()))

cnt = 0
for j in range(h):
    for i in range(w):
        if not isVisited[j][i]:
            dfs((j, i))
            cnt += 1

print(cnt)

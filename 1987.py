# https://www.acmicpc.net/problem/1987
from collections import deque


# up down left rigth
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
delta = [(0, -1), (0, 1), (-1, 0), (1, 0)]

R, C = map(int, input().split(" "))
graph = []
visited = [[0 for i in range(C)] for j in range(R)]

for _ in range(R):
    graph.append(list(input()))


def dfs(graph, visited, coor):
    alphaList = []
    stack = deque()
    stack.append(coor)
    visited[coor[0]][coor[1]] = 1
    alphaList.append(graph[coor[1]][coor[0]])

    while stack:
        y, x = stack.pop()
        alphaList.append(graph[y][x])

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < C and 0 <= ny < R:
                if graph[ny][nx] not in alphaList and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    stack.append((ny, nx))

    return alphaList


print(dfs(graph, visited, (0, 0)))
for line in visited:
    print(line)

# https://www.acmicpc.net/problem/10026
import sys

sys.setrecursionlimit(10000)
# up, down, left, right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(graph, node, isVisited, disable=False):
    y, x = node[0], node[1]
    isVisited[y][x] = True

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < N and 0 <= ny < N:
            if not isVisited[ny][nx]:
                if disable:
                    if graph[y][x] == "B":
                        if graph[y][x] == graph[ny][nx]:
                            dfs(graph, [ny, nx], isVisited, True)
                    else:
                        if graph[ny][nx] in ("G", "R"):
                            dfs(graph, [ny, nx], isVisited, True)
                else:
                    if graph[ny][nx] == graph[y][x]:
                        dfs(graph, [ny, nx], isVisited)


N = int(sys.stdin.readline())
board = []
isVisitedNormal = [[False for j in range(N)] for i in range(N)]
isVisitedDisabled = [[False for j in range(N)] for i in range(N)]

for _ in range(N):
    board.append(list(sys.stdin.readline()))

maxNormal = 0
maxDisabled = 0
for j in range(N):
    for i in range(N):
        if not isVisitedNormal[j][i]:
            dfs(board, [j, i], isVisitedNormal)
            maxNormal += 1

        if not isVisitedDisabled[j][i]:
            dfs(board, [j, i], isVisitedDisabled, True)
            maxDisabled += 1

print(f"{maxNormal} {maxDisabled}")

# https://www.acmicpc.net/problem/1012
import sys
from collections import deque

# up down left right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(graph, j, i):
    isVisited = []
    if graph[j][i] == 0:
        return 0

    toVisit = deque()
    isVisited.append((j, i))
    toVisit.append((j, i))

    while toVisit:
        node = toVisit.popleft()
        y, x = node[0], node[1]
        graph[y][x] = 0

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if (0 <= nx < M) and (0 <= ny < N):
                if (graph[ny][nx] == 1) and (ny, nx) not in isVisited:
                    isVisited.append((ny, nx))
                    toVisit.append((ny, nx))

    return 1


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split(" "))
    board = [[0 for i in range(M)] for j in range(N)]
    bachuList = []
    for _2 in range(K):
        x, y = map(int, sys.stdin.readline().split(" "))
        bachuList.append((y, x))
        board[y][x] = 1

    cnt = 0
    for node in bachuList:
        cnt += bfs(board, node[0], node[1])

    print(cnt)

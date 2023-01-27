import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
board = []
for _ in range(N):
    board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

# up down left right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(graph, j, i):
    toVisit = deque()
    toVisit.append((j, i))

    cnt = 0
    while toVisit:
        cnt += 1
        node = toVisit.popleft()
        # print("@", node)
        y, x = node[0], node[1]
        graph[y][x] = 0

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if (0 <= nx < N) and (0 <= ny < N):
                if graph[ny][nx] == 1 and [ny, nx] not in toVisit:
                    toVisit.append([ny, nx])
    return cnt


cityList = []
for i in range(N):
    for j in range(N):
        if board[j][i] == 1:
            # print("!", j, i)
            cityList.append(bfs(board, j, i))

print(len(cityList))
for city in sorted(cityList):
    print(city)

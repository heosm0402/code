# https://www.acmicpc.net/problem/2468
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
board = []

maxNumber = 1
for _ in range(N):
    temp_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    maxNumber = max(maxNumber, max(temp_list))
    board.append(temp_list)

# up down left right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(board, isVisted, coor, h):
    q = deque()
    q.append(coor)
    isVisted[coor[0]][coor[1]] = True
    maxlengthOfQueue = len(q)
    while q:
        maxlengthOfQueue = max(maxlengthOfQueue, len(q))
        node = q.popleft()
        y, x = node[0], node[1]
        isVisted[y][x] = True

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < N and 0 <= ny < N:
                if not isVisted[ny][nx] and board[ny][nx] > h:
                    # isVisted[ny][nx] = True
                    q.append((ny, nx))

    return maxlengthOfQueue

maxLand = 0
queueMaxLength = []
for h in range(maxNumber):
    cnt = 0
    isVisited = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if not isVisited[j][i] and board[j][i] > h:
                qLength = bfs(board, isVisited, (j, i), h)
                queueMaxLength.append(qLength)
                cnt += 1

    if maxLand < cnt:
        maxLand = cnt


print(maxLand)
print(queueMaxLength)
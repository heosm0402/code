# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().rstrip().split(" "))
isVisited = [[[False for _ in range(M)] for _2 in range(N)] for _3 in range(H)]

# front back left right up down
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

board = []
for _ in range(H):
    temp = []
    for _2 in range(N):
        temp.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    board.append(temp)

toVisit = deque()
for z in range(H):
    for y in range(N):
        for x in range(M):
            if board[z][y][x] == 1:
                toVisit.append((z, y, x))

while toVisit:
    node = toVisit.popleft()
    z, y, x = node[0], node[1], node[2]
    isVisited[z][y][x] = True
    for idx in range(6):
        nz = z + dz[idx]
        ny = y + dy[idx]
        nx = x + dx[idx]

        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if board[nz][ny][nx] == 0:
                board[nz][ny][nx] = board[z][y][x] + 1
                toVisit.append((nz, ny, nx))

maxNumber = 0
isZeroExist = False
for floor in board:
    for line in floor:
        if 0 in line:
            isZeroExist = True
        else:
            maxNumber = max(maxNumber, max(line))

if isZeroExist:
    print(-1)
else:
    print(maxNumber-1)

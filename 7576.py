# https://www.acmicpc.net/problem/7576
import sys
from collections import deque


# up down left right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
board = []
for _ in range(M):
    board.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

toVisit = deque()

for j in range(M):
    for i in range(N):
        if board[j][i] == 1:
            toVisit.append((j, i))

while toVisit:
    tomato = toVisit.popleft()
    y, x = tomato[0], tomato[1]

    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if (0 <= nx < N) and (0 <= ny < M):
            if board[ny][nx] == 0:

                toVisit.append((ny, nx))
                board[ny][nx] = board[y][x] + 1

maxNumber = 0
if any(0 in line for line in board):
    print(-1)
else:
    for line in board:
        maxNumber = max(maxNumber, max(line))
    print(maxNumber-1)

# https://www.acmicpc.net/problem/2583
import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().rstrip().split(" "))
delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
board = [[0 for i in range(N)] for j in range(M)]
for _ in range(K):
    lbx, lby, rtx, rty = map(int, sys.stdin.readline().rstrip().split(" "))
    for y in range(lby, rty):
        board[y][lbx:rtx] = ["X"] * (rtx - lbx)


def bfs(board, coor):
    cnt = 0
    board[coor[0]][coor[1]] = 1
    q = deque()
    q.append(coor)

    while q:
        y, x = q.popleft()
        cnt += 1
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if board[ny][nx] == 0:
                    board[ny][nx] = 1
                    q.append((ny, nx))

    return cnt


areaList = []
for y in range(M):
    for x in range(N):
        if board[y][x] == 0:
            areaList.append(bfs(board, (y, x)))

areaList = sorted(areaList)
print(len(areaList))
print(" ".join(map(str, areaList)))

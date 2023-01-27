# https://www.acmicpc.net/problem/1260
import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))


board = []
for _ in range(N):
	board.append(list(map(int, list(sys.stdin.readline().rstrip()))))

# up down left right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

toVisitList = [(0, 0)]
board[0][0] = 1
while toVisitList:
	coordinate = toVisitList.pop(0)
	# print(coordinate)
	x, y = coordinate[0], coordinate[1]

	for idx in range(4):
		nx = x + dx[idx]
		ny = y + dy[idx]

		if 0 <= nx < M and 0 <= ny < N:
			if board[ny][nx] == 1:
				toVisitList.append((nx, ny))
				board[ny][nx] = board[y][x] + 1

print(board[N-1][M-1])
# print(board)

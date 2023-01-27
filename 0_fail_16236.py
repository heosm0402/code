# https://www.acmicpc.net/problem/16236
from collections import deque


N = int(input())
delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]

board = []
sharkSize = 2
sharkAte = 0
sharkPosition = (0, 0)
for j in range(N):
    temp = list(map(int, input().split()))
    if 9 in temp:
        sharkPosition = (j, temp.index(9))
    board.append(temp)


def dfs(board, visited, coor):
    q = deque()
    q.append(coor)
    visited[coor[0]][coor[1]] = 0

    # fishList = set()
    minDist = 100
    minDistCoor = (0, 0)
    while q:
        y, x = q.popleft()

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0 <= ny < N and 0 <= nx < N:
                if board[ny][nx] <= sharkSize and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

                shouldChange = False
                if (board[ny][nx] < sharkSize) and board[ny][nx] != 0:
                    if visited[ny][nx] == minDist:
                        if ny < minDistCoor[0]:
                            shouldChange = True
                        elif ny == minDistCoor[0]:
                            if nx < minDistCoor[1]:
                                shouldChange = True
                    elif visited[ny][nx] < minDist:
                        shouldChange = True

                if shouldChange:
                    minDist = visited[ny][nx]
                    minDistCoor = (ny, nx)

    return minDist, minDistCoor


totalDist = 0
while 1:
    visited = [[0 for i in range(N)] for j in range(N)]
    minDist, minDistCoor = dfs(board, visited, sharkPosition)
    # print("@", nextFish)
    if minDist == 100:
        break
    board[sharkPosition[0]][sharkPosition[1]] = 0
    dist, sharkPosition = minDist, (minDistCoor[0], minDistCoor[1])
    totalDist += dist
    # print("#", dist, sharkPosition)
    board[sharkPosition[0]][sharkPosition[1]] = 9
    sharkAte += 1
    if sharkSize == sharkAte:
        sharkSize += 1
        sharkAte = 0

print(totalDist)

for line in board:
    print(line)
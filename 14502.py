# https://www.acmicpc.net/problem/14502
import copy
import sys
import itertools
from collections import deque, Counter

delta = ((0, -1), (0, 1), (-1, 0), (1, 0))
N, M = map(int, sys.stdin.readline().split(" "))

board = []
searchCoor = []
virusCoor = []
for j in range(N):
    temp = []
    elemList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    for i in range(M):
        temp.append(elemList[i])
        if elemList[i] == 0:
            searchCoor.append((j, i))
        if elemList[i] == 2:
            virusCoor.append((j, i))
    board.append(temp)

searchCombination = list(itertools.combinations(searchCoor, 3))


def dfs(graph, coor, isVisited):
    q = deque()
    q.extend(coor)

    while q:
        y, x = q.pop()
        isVisited[y][x] = 1

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0:
                    isVisited[ny][nx] = 1
                    graph[ny][nx] = 2
                    q.append((ny, nx))

    return graph


maxSafeArea = 0
for wall1, wall2, wall3 in searchCombination:
    copiedBoard = copy.deepcopy(board)
    isVisited = [[0] * M for _ in range(N)]

    copiedBoard[wall1[0]][wall1[1]] = 1
    copiedBoard[wall2[0]][wall2[1]] = 1
    copiedBoard[wall3[0]][wall3[1]] = 1

    result = dfs(copiedBoard, virusCoor, isVisited)

    flattenResult = list(itertools.chain.from_iterable(result))
    countedResult = Counter(flattenResult)
    # print(countedResult)
    zeroCount = countedResult.get(0)

    if zeroCount != None:
        maxSafeArea = max(maxSafeArea, zeroCount)

print(maxSafeArea)


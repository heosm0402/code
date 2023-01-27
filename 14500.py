# https://www.acmicpc.net/problem/14500
import sys


input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
board = []
boardTotalSum = 0
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

maxScore = 0
for y in range(N):
    for x in range(M):
        blockList = [
            # long
            [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)],
            [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)],

            # nemo
            [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)],

            # L
            [(x, y), (x, y + 1), (x, y + 2), (x + 1, y + 2)],
            [(x, y), (x, y + 1), (x, y + 2), (x - 1, y + 2)],
            [(x, y), (x, y - 1), (x, y - 2), (x + 1, y - 2)],
            [(x, y), (x, y - 1), (x, y - 2), (x - 1, y - 2)],
            [(x, y), (x + 1, y), (x + 2, y), (x + 2, y - 1)],
            [(x, y), (x + 1, y), (x + 2, y), (x + 2, y + 1)],
            [(x, y), (x - 1, y), (x - 2, y), (x - 2, y - 1)],
            [(x, y), (x - 1, y), (x - 2, y), (x - 2, y + 1)],

            # snake
            [(x, y), (x, y - 1), (x + 1, y - 1), (x + 1, y - 2)],
            [(x, y), (x, y - 1), (x - 1, y - 1), (x - 1, y - 2)],
            [(x, y), (x - 1, y), (x - 1, y - 1), (x - 2, y - 1)],
            [(x, y), (x - 1, y), (x - 1, y + 1), (x - 2, y + 1)],
            [(x, y), (x, y + 1), (x - 1, y + 1), (x - 1, y + 2)],
            [(x, y), (x, y + 1), (x + 1, y + 1), (x + 1, y + 2)],
            [(x, y), (x + 1, y), (x + 1, y - 1), (x + 2, y - 1)],
            [(x, y), (x + 1, y), (x + 1, y + 1), (x + 2, y + 1)],

            # mountain
            [(x, y), (x - 1, y), (x, y + 1), (x + 1, y)],
            [(x, y), (x - 1, y), (x, y + 1), (x, y - 1)],
            [(x, y), (x - 1, y), (x, y - 1), (x + 1, y)],
            [(x, y), (x, y - 1), (x + 1, y), (x, y + 1)]
        ]

        for b in blockList:
            inBoard = True
            blockSum = 0
            for p, q in b:
                if 0 <= p < M and 0 <= q < N:
                    blockSum += board[q][p]
                else:
                    inBoard = False

            if not inBoard:
                continue

            # if blockSum > maxScore:
            #     print(b)
            maxScore = max(maxScore, blockSum)

print(maxScore)

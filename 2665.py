import collections
import sys

delta = ((0, -1), (0, 1), (-1, 0), (1, 0))
n = int(sys.stdin.readline().rstrip())
maze = []
for _ in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))


def dfs(graph, isVisited, y, x):
    q = collections.deque()
    q.append((y, x))
    isVisited[y][x] = 1

    while q:
        y, x = q.pop()

        if y == x == n:
            return True

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n and not isVisited[ny][nx] and graph[ny][nx]:
                isVisited[ny][nx] = 1
                q.append((ny, nx))

    return False

cnt = 0

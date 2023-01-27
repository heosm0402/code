# https://www.acmicpc.net/problem/11724
import sys
from collections import deque
sys.setrecursionlimit(2500)

# up down left right
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(graph, node):
    toVisit = deque()
    toVisit.append(node)
    while toVisit:
        searching = toVisit.pop()
        isVisit[searching-1] = True
        for elem in graph.get(searching):
            if not isVisit[elem-1]:
                toVisit.append(elem)


N, M = map(int, sys.stdin.readline().split(" "))
graph = {i: set() for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph.get(a).add(b)
    graph.get(b).add(a)

isVisit = [False for i in range(N)]
cnt = 0
for node in range(1, N+1):
    if isVisit[node-1]:
        continue

    dfs(graph, node)
    cnt += 1
print(cnt)

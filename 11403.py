# https://www.acmicpc.net/problem/11403
import sys
from collections import deque


N = int(input())
graph = {}
for nodeNumber in range(N):
    nodeList = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    graph[nodeNumber] = [idx for idx, x in enumerate(nodeList) if x == 1]

canVisit = [[0 for i in range(N)] for j in range(N)]
for node in range(N):
    q = deque()
    q.append(node)

    firstTime = True
    while q:
        position = q.popleft()
        if not firstTime:
            canVisit[node][position] = 1
        for elem in graph[position]:
            if canVisit[node][elem] == 0:
                q.append(elem)
        firstTime = False

for line in canVisit:
    print(" ".join(map(str, line)))

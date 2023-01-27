# https://www.acmicpc.net/problem/11725
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = {number+1: [] for number in range(N)}
visited = [0 for number in range(N+1)]
for _ in range(N-1):
    elem1, elem2 = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[elem1].append(elem2)
    graph[elem2].append(elem1)

q = deque()
q.append(1)

parentNodeList = {}
while q:
    node = q.pop()
    visited[node] = 1

    for elem in graph.get(node):
        if not visited[elem]:
            parentNodeList[elem] = node
            q.append(elem)

for key, value in sorted(parentNodeList.items()):
    print(value)

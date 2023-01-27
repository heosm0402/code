# https://www.acmicpc.net/problem/5972
import heapq
import math
import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
graph = {i+1: [] for i in range(N)}
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(u).append((w, v))
    graph.get(v).append((w, u))

INF = math.inf
distList = [INF] * (N+1)
distList[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    cost, node = heapq.heappop(q)
    if distList[node] < cost:
        continue

    for nextCost, nextNode in graph.get(node):
        if cost + nextCost < distList[nextNode]:
            distList[nextNode] = cost + nextCost
            heapq.heappush(q, (cost + nextCost, nextNode))

# print(distList)
print(distList[N])

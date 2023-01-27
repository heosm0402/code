# https://www.acmicpc.net/problem/1916
import sys
import heapq


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
graph = {i+1: [] for i in range(N)}

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(u).append((w, v))

start, end = map(int, sys.stdin.readline().rstrip().split(" "))
INF = int(1e12)
distanceList = [INF] * (N+1)

q = []
heapq.heappush(q, (0, start))
distanceList[start] = 0

while q:
    cost, node = heapq.heappop(q)

    if distanceList[node] < cost:
        continue

    for nextCost, nextNode in graph.get(node):
        if distanceList[node] + nextCost < distanceList[nextNode]:
            distanceList[nextNode] = distanceList[node] + nextCost
            heapq.heappush(q, (distanceList[node] + nextCost, nextNode))

print(distanceList[end])

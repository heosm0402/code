# https://www.acmicpc.net/problem/11779
import heapq
import math
import sys


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = {i+1: [] for i in range(n)}

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(u).append((w, v))


start, end = map(int, sys.stdin.readline().rstrip().split(" "))

INF = math.inf
distList = [INF] * (n+1)
distList[start] = 0

cityList = [[] for _ in range(n+1)]
q = []
heapq.heappush(q, (0, start))
cityList[start] = [start]
while q:
    cost, node = heapq.heappop(q)
    if distList[node] < cost:
        continue

    for nextCost, nextNode in graph.get(node):
        if cost + nextCost < distList[nextNode]:
            cityList[nextNode] = cityList[node] + [nextNode]
            distList[nextNode] = cost + nextCost
            heapq.heappush(q, (cost+nextCost, nextNode))

print(distList[end])
print(len(cityList[end]))
print(" ".join(map(str, cityList[end])))

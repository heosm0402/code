# https://www.acmicpc.net/problem/1238
import heapq
import sys

N, M, X = map(int, sys.stdin.readline().rstrip().split(" "))
graph = {i+1: [] for i in range(N)}

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(u).append((w, v))

totalMaxDistList = []
for start in range(1, N+1):
    q = []
    heapq.heappush(q, (0, start))

    INF = int(1e12)
    distanceList = [INF] * (N+1)
    distanceList[start] = 0

    while q:
        cost, node = heapq.heappop(q)

        if distanceList[node] < cost:
            continue

        for nextCost, nextNode in graph.get(node):
            if distanceList[node] + nextCost < distanceList[nextNode]:
                distanceList[nextNode] = distanceList[node] + nextCost
                heapq.heappush(q, (distanceList[node] + nextCost, nextNode))

    totalMaxDistList.append(distanceList)

# for line in totalMaxDistList:
#     print(line)

comparisonList = []
for person in range(1, N+1):
    comparisonList.append(totalMaxDistList[person-1][X] + totalMaxDistList[X-1][person])

# print(comparisonList)
print(max(comparisonList))

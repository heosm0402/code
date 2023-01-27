# https://www.acmicpc.net/problem/1504
import heapq
import sys

N, E = map(int, sys.stdin.readline().rstrip().split(" "))
graph = {i + 1: [] for i in range(N)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(u).append((w, v))
    graph.get(v).append((w, u))

trans1, trans2 = map(int, sys.stdin.readline().rstrip().split(" "))


def getShortestDistance(start, end):
    q = []
    heapq.heappush(q, (0, start))

    INF = int(1e12)
    distanceList = [INF] * (N + 1)
    # print(start, "to ", end)
    # print(distanceList)
    distanceList[start] = 0
    # print("@", distanceList)

    while q:
        cost, node = heapq.heappop(q)
        if distanceList[node] < cost:
            continue

        for nextCost, nextNode in graph.get(node):
            if distanceList[node] + nextCost < distanceList[nextNode]:
                distanceList[nextNode] = distanceList[node] + nextCost
                # print("@", distanceList)
                heapq.heappush(q, (distanceList[node] + nextCost, nextNode))

    # print("end of ", distanceList, ":", distanceList[end])
    return distanceList[end]


result = min(
    getShortestDistance(1, trans1) + getShortestDistance(trans1, trans2) + getShortestDistance(trans2, N),
    getShortestDistance(1, trans2) + getShortestDistance(trans2, trans1) + getShortestDistance(trans1, N),
)

if result >= 1000000000000:
    print(-1)
else:
    print(result)

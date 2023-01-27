# https://www.acmicpc.net/problem/11404
import heapq
import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = {i+1:[] for i in range(n)}
busList = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(a).append((c, b))


def di(start):
    INF = int(1e9)
    distList = [INF] * (n+1)
    distList[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, node = heapq.heappop(q)
        if distList[node] < cost:
            continue

        for nextCost, nextNode in graph.get(node):
            if cost+nextCost < distList[nextNode]:
                distList[nextNode] = cost + nextCost
                heapq.heappush(q, (cost + nextCost, nextNode))

    return distList


for idx in range(n):
    result = di(idx+1)[1:]
    result = [0 if elem == 1000000000 else elem for elem in result]
    print(" ".join(map(str, result)))

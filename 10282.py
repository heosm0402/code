# https://www.acmicpc.net/problem/10282
import heapq
import sys


tc = int(sys.stdin.readline().rstrip())
for _ in range(tc):
    n, d, c = map(int, sys.stdin.readline().rstrip().split(" "))
    graph = {i+1:[] for i in range(n)}
    for __ in range(d):
        u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
        graph.get(v).append((w, u))

    INF = int(1e9)
    distList = [INF] * (n+1)
    distList[c] = 0

    q = []
    heapq.heappush(q, (0, c))
    while q:
        cost, node = heapq.heappop(q)

        if distList[node] < cost:
            continue

        for nextCost, nextNode in graph.get(node):
            if cost+nextCost < distList[nextNode]:
                distList[nextNode] = cost+nextCost
                heapq.heappush(q, (cost+nextCost, nextNode))

    # print(distList)
    computerCount = 0
    maxTime = 0
    for elem in distList:

        if elem == 1000000000:
            continue

        computerCount += 1
        maxTime = max(maxTime, elem)

    print(computerCount, maxTime)

# https://www.acmicpc.net/problem/9370
import heapq
import math
import sys
import time


def dijkstra(start, graph):
    INF = math.inf
    distList = [INF] * (n + 1)
    distList[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node = heapq.heappop(q)
        if distList[node] < cost:
            continue

        for nextCost, nextNode in graph.get(node):
            if cost + nextCost < distList[nextNode]:
                distList[nextNode] = cost + nextCost
                heapq.heappush(q, (cost + nextCost, nextNode))

    return distList


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split(" "))
    start, g, h = map(int, sys.stdin.readline().rstrip().split(" "))
    graph = {i + 1: [] for i in range(n)}
    for __ in range(m):
        u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
        graph.get(u).append((w, v))
        graph.get(v).append((w, u))

    targetCityList = []
    for _ in range(t):
        targetCityList.append(int(sys.stdin.readline().rstrip()))

    s = time.process_time()
    possbilityCity = []
    for targetCity in targetCityList:
        start_end = dijkstra(start, graph)[targetCity]
        start_g_h_end = dijkstra(start, graph)[g] + \
                        dijkstra(g, graph)[h] + \
                        dijkstra(h, graph)[targetCity]
        start_h_g_end = dijkstra(start, graph)[h] + \
                        dijkstra(h, graph)[g] + \
                        dijkstra(g, graph)[targetCity]

        if start_h_g_end == start_end or start_g_h_end == start_end:
            possbilityCity.append(targetCity)

    print(" ".join(map(str, sorted(possbilityCity))))

e = time.process_time()

print("Time elapsed: ", round(e - s, 8))
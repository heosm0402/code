# https://www.acmicpc.net/problem/9370
import heapq
import math
import sys

input = sys.stdin.readline

def d(start):
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
            if cost + nextCost < distList[nextNode]:
                distList[nextNode] = cost + nextCost
                heapq.heappush(q, (cost+nextCost, nextNode))

    return distList


T = int(input().rstrip())
for _ in range(T):
    n, m, t = map(int, input().rstrip().split(" "))
    start, g, h = map(int, input().rstrip().split(" "))
    graph = {i+1: [] for i in range(n)}
    for __ in range(m):
        u, v, w = map(int, input().rstrip().split(" "))
        graph.get(u).append((w, v))
        graph.get(v).append((w, u))

    fromStart = d(start)
    fromG = d(g)
    fromH = d(h)
    candidataCityList = []
    for __ in range(t):
        targetCity = int(input().rstrip())
        straight = fromStart[targetCity]
        # print(straight, fromStart[g] + fromG[h] + fromH[targetCity], fromStart[h] + fromH[g] + fromG[targetCity])
        if min(
                fromStart[g] + fromG[h] + fromH[targetCity],
                fromStart[h] + fromH[g] + fromG[targetCity]
        ) == straight:
            candidataCityList.append(targetCity)

    print(" ".join(map(str, sorted(candidataCityList))))


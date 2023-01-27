# https://www.acmicpc.net/problem/1162
import sys
import heapq
import math

N, M, K = map(int, sys.stdin.readline().rstrip().split(" "))
graph = {i+1: [] for i in range(N)}
START = 1

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph.get(u).append((w, v))
    graph.get(v).append((w, u))

INF = math.inf
distArray = [[INF] * (K+1) for _ in range(N+1)]
for i in range(K+1):
    distArray[START][i] = 0

q = []
heapq.heappush(q, (0, 1, 0))
while q:
    cost, node, paveCnt = heapq.heappop(q)
    # print("!", cost, node, paveCnt)
    if distArray[node][paveCnt] < cost:
        continue

    if paveCnt+1 <= K:
        for nextCost, nextNode in graph.get(node):
            if cost < distArray[nextNode][paveCnt+1]:
                # print(("@", node, nextNode, cost, paveCnt+1))
                distArray[nextNode][paveCnt+1] = cost
                heapq.heappush(q, (cost, nextNode, paveCnt+1))

    for nextCost, nextNode in graph.get(node):
        if cost + nextCost < distArray[nextNode][paveCnt]:
            distArray[nextNode][paveCnt] = cost + nextCost
            # print(("#", node, nextNode, cost + nextCost, paveCnt))
            heapq.heappush(q, (cost + nextCost, nextNode, paveCnt))

print(min(distArray[N]))

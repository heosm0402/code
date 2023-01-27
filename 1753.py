# https://www.acmicpc.net/problem/1753
import sys
import heapq
INF = int(1e9)
V, E = map(int, sys.stdin.readline().rstrip().split(" "))
K = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[u].append((w, v))

q = []
heapq.heappush(q, (0, K))
distance[K] = 0

while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
        continue

    for next_cost, next_node in graph[node]:
        cost = distance[node] + next_cost
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

for d in distance[1:]:
    if d != 1000000000:
        print(d)
    else:
        print("INF")

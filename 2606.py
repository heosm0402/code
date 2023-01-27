# https://www.acmicpc.net/problem/2606
import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())

graph = {}
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    if a in graph.keys():
        graph.get(a).append(b)
    else:
        graph[a] = [b]

    if b in graph.keys():
        graph.get(b).append(a)
    else:
        graph[b] = [a]

toVisit = [1]
visited = []
cnt = 0
while toVisit:
    computer = toVisit.pop(0)
    if computer not in visited:
        cnt += 1
        visited.append(computer)
        toVisit.extend(graph.get(computer))


print(cnt-1)

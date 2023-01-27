# https://www.acmicpc.net/problem/11650

import sys

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))

l.sort(key=lambda x: (x[0], x[1]))

for item in l:
    print(item[0], item[1])


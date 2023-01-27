# https://www.acmicpc.net/problem/11651

import sys

n = int(sys.stdin.readline())

l = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    l.append((a, b))

l.sort(key=lambda x: (x[1], x[0]))

for item in l:
    sys.stdout.write(str(item[0]) + ' ' + str(item[1]) + '\n')


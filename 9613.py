# https://www.acmicpc.net/problem/9613
import math
import sys

t = int(input())
for _ in range(t):
    l = list(map(int, sys.stdin.readline().split()))
    l.pop(0)

    r = 0
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            r += math.gcd(l[i], l[j])

    print(r)

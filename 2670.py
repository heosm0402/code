# https://www.acmicpc.net/problem/2670
import sys


N = int(sys.stdin.readline().rstrip())
l = []
for _ in range(N):
    l.append(float(sys.stdin.readline().rstrip()))

maxNumber = 0
for i in range(1, N):
    print(i, l[i-1], l[i], l[i]*l[i-1])
    l[i] = max(l[i], l[i] * l[i-1])

print(l)
print("%0.3f" % max(l))

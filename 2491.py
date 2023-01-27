# https://www.acmicpc.net/problem/2491
import sys

N = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split(" ")))
ll = []
for idx in range(len(l)-1):
    ll.append(l[idx+1] - l[idx])

ascStack = 1
descStack = 1
maxStack = 1
for idx in range(len(l)-1):
    diff = l[idx+1] - l[idx]
    if diff == 0:
        ascStack += 1
        descStack += 1
    elif diff > 0:
        ascStack += 1
        descStack = 1
    else:
        descStack += 1
        ascStack = 1

    maxStack = max(maxStack, ascStack, descStack)

print(maxStack)

# https://www.acmicpc.net/problem/1302
import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
l = []
for _ in range(N):
    l.append(sys.stdin.readline().rstrip())

result = Counter(l)
sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
print(sorted_result[0][0])

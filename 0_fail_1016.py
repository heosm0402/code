# https://www.acmicpc.net/problem/1016

import math as m

a, b = map(int, input().split())

r = []
for i in range(a, b+1):
    if int(m.sqrt(i)) != m.sqrt(i):
        r.append(i)
    else:
        pass


print(r)

print(len(r))
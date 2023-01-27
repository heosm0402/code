# https://www.acmicpc.net/problem/1676
import math

f = str(math.factorial(int(input())))
r = 0
for e in f[::-1]:
    if e == "0":
        r += 1
    else:
        break

print(r)

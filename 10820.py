# https://www.acmicpc.net/problem/10820
import sys

lines = sys.stdin.readlines()

for line in lines:
    l = map(ord, list(line))

    r = [0, 0, 0, 0]
    for e in l:
        if e == 32:
            r[3] += 1
        elif 48 <= e <= 57:
            r[2] += 1
        elif 65 <= e <= 90:
            r[1] += 1
        elif 97 <= e <= 122:
            r[0] += 1

    print(" ".join(map(str, r)))

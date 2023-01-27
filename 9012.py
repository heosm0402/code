# https://www.acmicpc.net/problem/9012
import sys

t = int(input())
for _ in range(t):
    l = list(sys.stdin.readline().rstrip())
    vps = 0
    b = False
    for ps in l:
        if ps == "(":
            vps += 1
        else:
            vps -= 1

        if vps < 0:
            b = True

        if b:
            break

    if vps == 0:
        print("YES")
    else:
        print("NO")

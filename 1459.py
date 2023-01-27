# https://www.acmicpc.net/problem/1459
import sys

X, Y, W, S = map(int, sys.stdin.readline().split(" "))

move1 = (X+Y) * W
if (X+Y) % 2 == 0:
    move2 = max(X, Y) * S
else:
    move2 = (max(X, Y) - 1) * S + W

move3 = min(X, Y) * S + abs(X - Y) * W

print(min(move1, move2, move3))

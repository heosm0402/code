# https://www.acmicpc.net/problem/9093
import sys


def reverse(e):
    return e[::-1]


n = int(input())
for _ in range(n):
    l = list(map(reverse, sys.stdin.readline().split()))
    print(" ".join(l))

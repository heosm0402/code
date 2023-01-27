# https://www.acmicpc.net/problem/16562
import sys


N, M, k = map(int, sys.stdin.readline().rstrip().split(" "))
moneyList = list(map(int, sys.stdin.readline().rstrip().split(" ")))

freindList = []
for idx in range(M):
    v, w = map(int, sys.stdin.readline().rstrip().split(" "))

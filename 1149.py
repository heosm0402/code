# https://www.acmicpc.net/problem/1149
import sys

N = int(sys.stdin.readline().rstrip())
price = []

for _ in range(N):
    price.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    

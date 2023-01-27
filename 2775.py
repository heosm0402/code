# https://www.acmicpc.net/problem/2775
import sys


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    apartment = [[0 for i in range(n)] for j in range(k+1)]
    apartment[0] = [i+1 for i in range(n)]
    for fl in range(1, k+1):
        for roomNum in range(0, n):
            apartment[fl][roomNum] = sum(apartment[fl-1][:roomNum+1])

    # for l in apartment:
    #     print(l)
    print(apartment[k][n-1])

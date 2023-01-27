# https://www.acmicpc.net/problem/6064
import sys

read = sys.stdin.readline
T = int(read())

for _ in range(T):
    M, N, x, y = map(int, read().split())

    year = 1
    while 1:
        if (year == (year // M) * M + x) and (year == (year // N) * N + y):
            answer = (year // M) * M + x
            break
        else:
            year += 1

        if year > (N * M) + 1:
            answer = -1
            break

    print(answer)

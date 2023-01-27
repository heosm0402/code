# https://www.acmicpc.net/problem/1978
import math

N = int(input())
l = list(map(int, input().split()))
r = 0


def isPrimeNumber(n):
    if n == 1:
        return 0

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0

    return 1


for n in l:
    r += isPrimeNumber(n)

print(r)

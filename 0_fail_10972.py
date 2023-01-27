# https://www.acmicpc.net/problem/10972
from itertools import permutations


N = int(input())
target = tuple(map(int, input().split()))
comb = list(permutations(range(1, N+1), N))

if len(comb) == comb.index(target)+1:
    print(-1)
else:
    print(" ".join(map(str, comb[comb.index(target)+1])))

# https://www.acmicpc.net/problem/2309

from itertools import combinations

l = []
for _ in range(9):
    l.append(int(input()))

total_sum = sum(l)
combination = list(combinations(l, 2))
for comb in combination:
    if total_sum - sum(comb) == 100:
        for h in comb:
            l.remove(h)
        break

for i in sorted(l):
    print(i)

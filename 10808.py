# https://www.acmicpc.net/problem/10808
import collections

s = list(input().rstrip())
alpha = "abcdefghijklmnopqrstuvwxyz"

col = collections.Counter(s)
for al in alpha:
    if al in col:
        print(col.get(al), end=' ')
    else:
        print("0", end=' ')

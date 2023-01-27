# https://www.acmicpc.net/problem/2750

n = int(input())

l = []
for idx in range(n):
    i = int(input())
    l.append(i)

l.sort()

for item in l:
    print(item)

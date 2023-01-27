# https://www.acmicpc.net/problem/1026

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)


S = 0
for idx in range(len(a)):
    result_multiple = a[idx] * b[idx]
    S += result_multiple

print(S)
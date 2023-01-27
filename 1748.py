# https://www.acmicpc.net/problem/1748

N = int(input())

lenOfN = len(str(N))
if lenOfN == 1:
    print(N)
    exit(0)

answer = 0
for i in range(lenOfN):
    if i+1 == lenOfN:
        answer += (N - (10 ** i) + 1) * (i + 1)
    else:
        answer += ((10 ** (i+1)) - (10 ** i)) * (i + 1)

print(answer)

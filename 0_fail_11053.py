# https://www.acmicpc.net/problem/11053


n = int(input())
l = list(map(int, input().split()))

dp = [l[0]]
longest = 0

for idx in range(len(l)):
    if dp[-1] < l[idx]:
        dp.append(l[idx])
    else:
        longest = max(longest, len(dp))
        dp = [l[idx]]


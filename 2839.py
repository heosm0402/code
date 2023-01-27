# https://www.acmicpc.net/problem/2839
import sys

N = int(sys.stdin.readline().rstrip())
dp = [0] * (N+1)
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

for i in range(6, N+1):
    if i % 5 == 0:
        dp[i] = dp[i-5] + 1
    elif i % 3 == 0:
        dp[i] = dp[i-3] + 1
    else:
        if dp[i-3] != 0 and dp[i-5] != 0:
            dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])

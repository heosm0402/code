# https://www.acmicpc.net/problem/14495

n = int(input())

dp = [0] * 117
dp[1] = 1
dp[2] = 1
dp[3] = 1
if n <= 3:
    print(dp[n])
    exit(0)

for idx in range(4, n+1):
    dp[idx] = dp[idx-1] + dp[idx-3]

print(dp[n])

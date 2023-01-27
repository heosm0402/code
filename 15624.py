# https://www.acmicpc.net/problem/15624

n = int(input())
if n <= 1:
    print(n)
    exit(0)

dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[n])

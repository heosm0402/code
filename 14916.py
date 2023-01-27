# https://www.acmicpc.net/problem/14916

n = int(input())

if n < 3:
    dp = [10000000] * 4
else:
    dp = [10000000] * (n+1)

dp[1] = -1
dp[2] = 1
dp[3] = -1

if n <= 3:
    print(dp[n])
    exit(0)

for i in range(4, n+1):
    if i % 2 == 0:
        dp[i] = i // 2

    if i % 5 == 0:
        dp[i] = i // 5

    if (i-2) % 5 == 0:
        dp[i] = min(dp[i], dp[i-2]+1)

    if (i-2) % 2 == 0:
        dp[i] = min(dp[i], dp[i-2]+1)

    if (i-5) % 2 == 0:
        dp[i] = min(dp[i], dp[i-5]+1)

    if (i-5) % 5 == 0:
        dp[i] = min(dp[i], dp[i-5]+1)

    if dp[i] == 10000000:
        dp[i] = -1

print(dp[n])

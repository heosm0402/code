# https://www.acmicpc.net/problem/1788

n = int(input())
if n == 0:
    print(0)
    print(0)
    exit(0)

dp = [0] * 1000001
dp[0] = 0
dp[1] = 1

for i in range(2, 1000001):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

if n > 0:
    print(1)
    print(dp[n])
else:
    n *= -1

    if n % 2 == 0:
        print(-1)
        print(dp[n])
    else:
        print(1)
        print(dp[n])

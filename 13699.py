# https://www.acmicpc.net/problem/13699

n = int(input())
if n <= 1:
    print(1)
    exit(0)

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    temp = 0
    for j in range(i):
        a = dp[j]
        b = dp[i-j-1]
        temp += a * b

    dp[i] = temp

print(dp[n])

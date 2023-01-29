# https://www.acmicpc.net/problem/11052


n = int(input())
p = list(map(int, input().split()))
p.insert(0, 1)
dp = [0] * (n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])

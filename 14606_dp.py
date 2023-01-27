# https://www.acmicpc.net/problem/14606

N = int(input())
dp = [0, 0, 1, 3]

for idx in range(4, N+1):
    half = idx // 2
    anotherHalf = idx - half

    dp.append((half*anotherHalf) + dp[half] + dp[anotherHalf])

print(dp[N])

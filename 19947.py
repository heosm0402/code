# https://www.acmicpc.net/problem/19947

H, Y = map(int, input().split(" "))
if Y == 0:
    print(H)
    exit(0)

dp = [H] + [0] * 10
dp[1] = int(dp[0] * 1.05)
dp[2] = int(dp[1] * 1.05)
dp[3] = int(max(dp[2] * 1.05, dp[0] * 1.2))
dp[4] = int(max(dp[3] * 1.05, dp[1] * 1.2))
dp[5] = int(max(dp[4] * 1.05, dp[2] * 1.2, dp[0] * 1.35))

for idx in range(6, Y+1):
    dp[idx] = int(max(dp[idx-1] * 1.05, dp[idx-3] * 1.2, dp[idx-5] * 1.35))

print(dp[Y])

# https://www.acmicpc.net/problem/13301
import sys

N = int(sys.stdin.readline().rstrip())

dp = [0, 1, 1, 2] + [0] * (N+1-3)

for idx in range(4, N+2):
    dp[idx] = dp[idx-2] + dp[idx-1]

# print(dp)
if N == 1:
    print(4)
elif N == 2:
    print(6)
elif N == 3:
    print(10)
else:
    print(2 * (dp[N] + dp[N+1]))

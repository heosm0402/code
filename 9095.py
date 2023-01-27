# https://www.acmicpc.net/problem/9095
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if N == 1:
        print(1)
        continue
    elif N == 2:
        print(2)
        continue
    elif N == 3:
        print(4)
        continue
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])

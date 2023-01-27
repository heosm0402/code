# https://www.acmicpc.net/problem/16395

n, k = map(int, input().split(" "))

if n <= 2:
    print(1)
    exit(0)

dp = [[0]]
dp.append([1])
dp.append([1, 1])

for i in range(3, n+1):
    temp = [1]
    for j in range(len(dp[i-1])-1):
        temp.append(dp[i-1][j] + dp[i-1][j+1])
    temp.append(1)
    dp.append(temp)

print(dp[n][k-1])

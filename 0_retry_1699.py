# https://www.acmicpc.net/problem/1699
# 입력예제: 82009 출력예제: 2
import math
import time

n = int(input())

# min 연산, ** 연산의 차이로 인해 시간 차이 발생
# 가장 오래 걸리는 loop
s = time.time()
dp = [n for n in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    for j in range(1, int(i**0.5)+1):
        dp[i] = min(dp[i], dp[i-j**2]+1)

print(dp[n])
print(time.time() - s)

# 가장 빠른 loop
s = time.time()
dp = [n for n in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n+1):
    for j in range(1, int(i ** 0.5) + 1):
        if dp[i-j*j]+1 < dp[i]:
            dp[i] = dp[i-j*j]+1

print(dp[n])
print(time.time() - s)

# math.sqrt vs **0.5 연산 -> 비슷함
s = time.time()
dp = [n for n in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 3
for i in range(4, n+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        if dp[i-j*j]+1 < dp[i]:
            dp[i] = dp[i-j*j]+1

print(dp[n])
print(time.time() - s)

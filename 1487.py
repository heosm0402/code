# https://www.acmicpc.net/problem/1487
import sys

N = int(sys.stdin.readline().rstrip())

person = []
for _ in range(N):
    person.append(tuple(map(int, sys.stdin.readline().rstrip().split(" "))))

person.sort(key=lambda x: (x[0], x[1]))

maxProfit = 0
effectivePrice = 0
peopleCount = N
for i in range(0, N):
    price = person[i][0]
    totalProfit = 0

    for j in range(i, N):
        profit =  price - person[j][1]
        if profit > 0:
            totalProfit += profit
    # print(i, price, totalProfit)

    if totalProfit < 0:
        continue

    if maxProfit < totalProfit:
        maxProfit = totalProfit
        effectivePrice = price

    if maxProfit == totalProfit:
        effectivePrice = min(effectivePrice, price)

print(effectivePrice)

# https://www.acmicpc.net/problem/1246
import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
priceList = []
for _ in range(M):
    priceList.append(int(sys.stdin.readline().rstrip()))

sortedPriceList = sorted(priceList, reverse=True)

maxProfit = 0
lastPrice = 0
for idx in range(len(sortedPriceList)):
    eggs = min(N, idx+1)
    price = sortedPriceList[idx]
    profit = eggs * price
    # print(eggs, price, profit)
    if maxProfit <= profit:
        maxProfit = profit
        lastPrice = price

print(lastPrice, maxProfit)

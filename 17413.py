# https://www.acmicpc.net/problem/17413
import re


s = input().rstrip()
answer = ""
tempWord = ""

isTaged = False
for elem in s:
    if elem == "<":
        answer += tempWord[::-1]
        tempWord = ""
        isTaged = True

    if elem == " ":
        answer += tempWord[::-1]

        tempWord = ""
        answer += elem
        continue

    if isTaged:
        answer += elem
    else:
        tempWord += elem

    if elem == ">":
        isTaged = False

if tempWord != "":
    answer += tempWord[::-1]

print(answer)

# https://www.acmicpc.net/problem/14606
import copy

towerArray = [int(input())]
pleasure = 0

while 1:
    temp = []
    for tower in towerArray:
        if tower == 1:
            continue

        half = tower // 2

        temp.append(half)
        if tower % 2 == 0:
            temp.append(half)
            pleasure += half * half
        else:
            temp.append(half + 1)
            pleasure += half * (half+1)

    if len(temp) == sum(temp):
        break

    towerArray = copy.deepcopy(temp)

print(pleasure)

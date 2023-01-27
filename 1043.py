# https://www.acmicpc.net/problem/1043
import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
knownPeopleInfo = list(map(int, sys.stdin.readline().rstrip().split(" ")))
knownPeopleCount, knownPeopleList = knownPeopleInfo[0], knownPeopleInfo[1:]
parentInfo = [i for i in range(N+1)]

if N == 0:
    print(M)
    exit(0)


def findParent(x):
    if parentInfo[x] == x:
        return x
    else:
        return findParent(parentInfo[x])


def union(a, b):
    a = findParent(a)
    b = findParent(b)

    if a in knownPeopleList and b in knownPeopleList:
        return
    elif a in knownPeopleList:
        parentInfo[b] = a
    elif b in knownPeopleList:
        parentInfo[a] = b
    else:
        if a < b:
            parentInfo[b] = a
        else:
            parentInfo[a] = b


partyList = []
for _ in range(M):
    partyInfo = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    partyPeopleCount, partyPeople = partyInfo[0], partyInfo[1:]
    partyList.append((partyPeopleCount, partyPeople))
    for idx in range(partyPeopleCount-1):
        union(partyPeople[idx], partyPeople[idx+1])

cnt = 0
for partyPeopleCount, partyPeople in partyList:
    for person in partyPeople:
        if findParent(person) in knownPeopleList:
            break
    else:
        cnt += 1

print(cnt)

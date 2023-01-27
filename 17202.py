import copy
import sys

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())

summation = []
for idx in range(len(A)):
    summation.append(A[idx])
    summation.append(B[idx])

while 1:
    l = len(summation)
    temp = []
    for idx in range(l-1):
        temp.append((int(summation[idx]) + int(summation[idx+1])) % 10)

    summation = copy.deepcopy(temp)
    if len(summation) == 2:
        break

print(str(summation[0]) + str(summation[1]))

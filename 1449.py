# https://www.acmicpc.net/problem/1449
import sys

N, L = map(int, sys.stdin.readline().rstrip().split(" "))
broken = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))

attachedTape = {}
for idx in range(N):
    target = broken[idx]
    startPoint = target - 0.5
    endPoint = target + 0.5
    if idx == 0:
        attachedTape[startPoint] = target + L - 0.5
        continue

    alreadyFixed = False
    for k, v in attachedTape.items():
        if k <= startPoint and endPoint <= v:
            alreadyFixed = True
            break

    if not alreadyFixed: attachedTape[startPoint] = target + L - 0.5

print(len(attachedTape))

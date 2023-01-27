# https://www.acmicpc.net/problem/15652


N, M = map(int, input().split())
s = []


def backTracking():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(1, N+1):
        if len(s) != 0:
            if s[-1] > i:
                continue

        s.append(i)
        backTracking()
        s.pop()


backTracking()

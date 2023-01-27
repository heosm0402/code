# https://www.acmicpc.net/problem/15656


N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
s = []


def backTracking():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for k in l:
        s.append(k)
        backTracking()
        s.pop()


backTracking()

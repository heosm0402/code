# https://www.acmicpc.net/problem/15657


N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
s = []


def backTracking():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for k in l:
        if len(s) != 0 and s[-1] > k:
            continue

        s.append(k)
        backTracking()
        s.pop()


backTracking()

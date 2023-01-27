# https://www.acmicpc.net/problem/15655


N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
visited = [False] * (l[-1] + 1)
s = []


def backTracking():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for k in l:
        if visited[k]:
            continue

        if len(s) != 0 and s[-1] > k:
            continue

        visited[k] = True
        s.append(k)
        backTracking()
        s.pop()
        visited[k] = False


backTracking()

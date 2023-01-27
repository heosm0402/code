# https://www.acmicpc.net/problem/15654


N, M = map(int, input().split())
l = sorted(list(map(int, input().split())))
s = []
visited = [False] * (l[-1] + 1)


def backTracking():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for k in l:
        if visited[k]:
            continue

        visited[k] = True
        s.append(k)
        backTracking()
        s.pop()
        visited[k] = False


backTracking()

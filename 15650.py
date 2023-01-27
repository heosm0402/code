# https://www.acmicpc.net/problem/15650


N, M = map(int, input().split())
s = []
visited = [False] * (N+1)


def backTracking():
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(1, N+1):
        if visited[i]:
            continue

        if len(s) != 0 and s[-1] > i:
            continue

        visited[i] = True
        s.append(i)
        backTracking()
        s.pop()
        visited[i] = False


backTracking()

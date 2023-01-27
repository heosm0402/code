# https://www.acmicpc.net/problem/18290


n, m, k = map(int, input().split())
s = []
l = []
visited = [[False for i in range(m)] for j in range(n)]
maxScore = 0
for _ in range(n):
    l.append(list(map(int, input().split())))


def backTracking():
    if len(s) == k:
        global maxScore
        score = 0
        for y, x in s:
            score += l[y][x]

        maxScore = max(score, maxScore)
        return

    for x in range(m):
        for y in range(n):

            delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            near = False
            for ny, nx in s:
                for dy, dx in delta:
                    if ny == y + dy and nx == x + dx:
                        near = True
                        break

                if near:
                    break

            if near:
                continue

            s.append((y, x))
            backTracking()
            s.pop()


backTracking()
print(maxScore)

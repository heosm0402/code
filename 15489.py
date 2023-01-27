# https://www.acmicpc.net/problem/15489

r, c, w = map(int, input().split(" "))
tri = [[0] * 30 for i in range(30)]
tri[0][0] = 1
tri[1][0] = 1
tri[1][1] = 1

for i in range(2, 30):
    tri[i][0] = 1
    for j in range(i-1):
        tri[i][j+1] = tri[i-1][j] + tri[i-1][j+1]

    tri[i][i] = 1

summation = 0
for b, i in enumerate(range(r-1, r-1+w)):
    for j in range(c-1, c+b):
        # print(i, j)
        summation += tri[i][j]

print(summation)

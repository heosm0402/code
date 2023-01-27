# https://www.acmicpc.net/problem/10809


s = list(input().rstrip())
a = list("abcdefghijklmnopqrstuvwxyz")
for i in a:
    if i in s:
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')

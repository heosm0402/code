# https://www.acmicpc.net/problem/1759


L, C = map(int, input().split())
alpha = sorted(input().split())
s = []


def backTracking():
    vowel = {'e', 'i', 'o', 'a', 'u'}
    if len(s) == L and (len(set(s).difference(vowel)) >= 2) and (len(set(s).intersection(vowel)) >= 1):
        print("".join(s))
        return

    for char in alpha:
        if char in s:
            continue

        if len(s) != 0 and s[-1] > char:
            continue

        s.append(char)
        backTracking()
        s.pop()


backTracking()

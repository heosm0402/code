# https://www.acmicpc.net/problem/11656

s = input()

r = []
for i in range(len(s)):
    r.append(s[i:])

print("\n".join(sorted(r)))

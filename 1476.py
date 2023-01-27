
e, s, m = map(int, input().split(" "))

a = 1
while 1:
    if (a-e) % 15 == 0 and (a-s) % 28 == 0 and (a-m) % 19 == 0:
        break
    else:
        a += 1

print(a)

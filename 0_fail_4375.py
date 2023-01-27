# https://www.acmicpc.net/problem/4375

n = int(input())

cnt = 1
a = 1
while 1:
	if a % n == 0:
		break

	if a // n == 0:
		a = (a % n) * 10 + 1
		cnt += 1
	else:
		a = a % n

print(cnt)

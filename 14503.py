# https://www.acmicpc.net/problem/14503

import sys

height, width = map(int, sys.stdin.readline().split())
y, x, direction = map(int, sys.stdin.readline().split())

area = []
for _ in range(height):
    area.append(list(map(int, sys.stdin.readline().split())))


class robot():
    def __init__(self, y, x, direction):
        self.y = y
        self.x = x
        self.direction = direction


    def turn(self):
        if self.direction != 0:
            self.direction -= 1
        else:
            self.direction += 3



cond = True
cnt = 0
while cond:
    cnt += 1 # clean up
    area[y][x] = 2 # check cleaned area






print(area)


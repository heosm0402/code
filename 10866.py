# https://www.acmicpc.net/problem/10866
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
q = deque()

for _ in range(n):
    input = sys.stdin.readline().rstrip()
    try:
        command, number = input.split(" ")
    except:
        command = input.rstrip()

    if command == "push_front":
        q.appendleft(number)
    elif command == "push_back":
        q.append(number)
    elif command == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif command == "back":
        try:
            print(q[-1])
        except:
            print(-1)
    elif command == "pop_front":
        try:
            print(q.popleft())
        except:
            print(-1)
    elif command == "pop_back":
        try:
            print(q.pop())
        except:
            print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if len(q):
            print(0)
        else:
            print(1)

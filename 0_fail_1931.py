# https://www.acmicpc.net/problem/1931
import sys

N = int(input())
meetingList = [tuple(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(N)]
# meetingList.sort(key=lambda x: x[0])
# print(meetingList)
meetingList.sort(key=lambda x: x[1])
print(meetingList)

meetingSchedule = [meetingList[0]]
lastMeeting = meetingSchedule[-1]
for i in range(1, N):
    if lastMeeting[1] <= meetingList[i][0]:
        meetingSchedule.append(meetingList[i])
        lastMeeting = meetingSchedule[-1]

print(len(meetingSchedule))

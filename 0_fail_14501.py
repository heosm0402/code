# https://www.acmicpc.net/problem/14501


N = int(input())
tasks = {}
for day in range(1, N+1):
    t, p = map(int, input().split())
    tasks[day] = {'t': t, 'p': p}

maxProfit = 0


def backTracking(day):
    global maxProfit

    if len(schedule) == 0 and day + tasks.get(day).get('t') <= N+1:
        schedule.append(day)

    recentNextTask = day + tasks.get(day).get('t')
    if tasks.get(recentNextTask) is None or recentNextTask + tasks.get(recentNextTask).get('t') > N+1:
        profit = 0
        for s in schedule:
            profit += tasks.get(s).get('p')
        maxProfit = max(profit, maxProfit)
        return

    for d in range(recentNextTask, N+1):
        if d >= day + tasks.get(day).get('t') and d + tasks.get(d).get('t') <= N+1:
            schedule.append(d)
            backTracking(d)
            schedule.pop()


for i in range(1, N+1):
    schedule = []
    backTracking(i)

print(maxProfit)

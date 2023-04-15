'''
swap이 없는 시험이 없네
'''
def solution(schedule):
    answer = 0
    for i in range (len(schedule)):
        if schedule[i][0] > 5:
            schedule[i][2] += 5

    for i in range(len(schedule) - 1, 0, -1):
        for j in range(0, i):
            if schedule[j][2] > schedule[j + 1][2]:
                temp = schedule[j]
                schedule[j] = schedule[j + 1]
                schedule[j + 1] = temp

    t = 0
    for i in range (len(schedule)):
        if t <= schedule[i][1]:
            answer += 1
            t = schedule[i][2]

    return answer
'''
열번호, 중앙에 가까운 순으로 배치
'''
def solution(seats):
    for i in range(len(seats)-1, 0, -1):
        for j in range(0, i):
            if seats[j][1] > seats[j + 1][1]:
                temp = seats[j]
                seats[j] = list(seats[j + 1])
                seats[j + 1] = list(temp)
            elif seats[j][1] == seats[j + 1][1]:
                if abs(seats[j][0] - 15) > abs(seats[j + 1][0] - 15):
                    temp = seats[j]
                    seats[j] = list(seats[j + 1])
                    seats[j + 1] = list(temp)

    return list(seats)

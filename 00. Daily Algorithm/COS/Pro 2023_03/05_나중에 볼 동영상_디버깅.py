'''
1줄 고치기
while day > 3: --> while len(q) != 0 and day - q[0] > 3: 수정함
'''

def solution(watch):
    answer = 0
    q = []
    day = 1

    for i in range(0, len(watch)):
        while len(q) != 0 and day - q[0] > 3:
            q.pop(0)
            answer += 1
        if watch[i] == 1:
            q.append(day)
        elif  len(q) != 0 and watch[i] == 0:
            q.pop(0)
        day += 1
    answer += len(q)
    return answer
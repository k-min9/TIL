from collections import deque

def str_to_time(str):
    h = int(str[:2])
    m = int(str[3:5])
    return h*60 + m

def time_to_str(int):
    h = str(int//60)
    if len(h) == 1:
        h = '0'+ h
    m = str(int%60)
    if len(m) == 1:
        m = '0'+ m
    return h+':'+m

def solution(n, t, m, timetable):
    # 섞고
    timetable = list(map(str_to_time, timetable))
    timetable.sort()
    timetable = deque(timetable)
    
    # 시작은 9시, 밑에서 부터 갱신시 최대한 게으른 출발시간 확인 가능
    start = 540
    answer = 0
    for _ in range(n):
        for _ in range(m):
            # 1분 빨리
            if timetable and timetable[0] <= start:
                answer = timetable.popleft() - 1
            # 저스트 도착
            else:
                answer = start
        start = start + t
    
    return time_to_str(answer)
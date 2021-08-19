'''
스케쥴 무지성으로 박아서 죄다 더해도 될 거 같은데... >> 되네
'''
import sys
input = sys.stdin.readline

N =int(input())
times = []
for _ in range(N):
    t, s = map(int, input().split())
    times.append([t, s])


# 마감시간 오름차순
times.sort(key= lambda x : x[1])

# 1차 시작 시간
start = times[0][1]
cur = start

# 모자란 시간 만큼 뺀다.
for need, deadline in times:
    cur = cur + need
    # 시간 내에 안되겠는데요
    if deadline < cur:
        #잠을 줄여라
        start = start - cur + deadline
        if start < 0:
            start = -1
            break
        cur = deadline

print(start)


'''
8시 이후 취침 새벽 2시 기상이 늦잠...?
'''
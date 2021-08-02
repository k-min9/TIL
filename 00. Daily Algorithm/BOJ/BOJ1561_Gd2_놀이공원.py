'''
나도 놀이공원에서 놀고싶다!
'''

import sys
input = sys.stdin.readline

# 사람 수, 놀이기구 종류 수
N, M = map(int, input().split())
times = list(map(int, input().split()))

# 최대 인원수 * 최대 운행시간 + 1 부터 이진 탐색
left = 0
right = 2000000000 * 30 + 1

# 사람 수 보다 적으면 빠르게 끝내기
if N <= M:
    print(N)
    exit()

# 딱 N명을 태울때까지만 굴리면 되나...?
while left<=right:
    mid = (left+right) // 2
    # mid 까지 탑승자 수 (0초에 M명 탑승)
    cnt = M
    for i in range(M):
        cnt = cnt + (mid // times[i])
    # print('2', cnt)
    # N 이상 > 커트 낮추기
    if cnt >= N:
        time = mid  # 이거 안하면 -1로 기록 될 수 있더라
        right = mid - 1
    # N 미만 > 커트 올리기
    else:
        left = mid + 1

# time 계산 완료 >> 시뮬레이팅
# print('1', time)

# time - 1 까지 탑승자 수 계산
cnt = M  
for i in range(M):
    cnt = cnt + (time - 1) // times[i]

# time때 일어난 일 시뮬레이팅
for i in range(M):
    if time % times[i] == 0:
        cnt = cnt + 1
        # 올린김에 N명째인지 체크
        if cnt == N:
            print(i + 1)
            break




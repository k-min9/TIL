'''
투포인트.
'''

import sys
input = sys.stdin.readline

# 사람 수,  풍선 수, 속도
N, M = map(int, input().split())
times = list(map(int, input().split()))

# 최대 인원수 * 최대 제작 시간 + 1 부터 이진 탐색
left = 0
right = 1000000 * 1000000 + 1


# 딱 M개의 풍선을 만드는데 걸리는 시간
while left<=right:
    mid = (left+right) // 2
    # mid 까지 제작한 풍선 수
    cnt = 0
    for i in range(N):
        cnt = cnt + (mid // times[i])
    # M 이상 > 커트 낮추기
    if cnt >= M:
        time = mid  # 이거 안하면 -1로 기록 될 수 있더라
        right = mid - 1
    # M 미만 > 커트 올리기
    else:
        left = mid + 1

# time 계산 완료 >> 시뮬레이팅
print(time)


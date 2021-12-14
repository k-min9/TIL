'''
구하려는 값을 mid에 두고 이분 탐색!
'''
import sys
input = sys.stdin.readline

# 탈출구 까지 거리, 돌섬 수, 제거 가능 돌섬 수
D, N, M = map(int, input().split())
islands = [int(input()) for _ in range(N)]
islands.sort()


answer = 0
lo, hi = 0, D
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = 0  # 돌 수
    now = 0  # 이동 후 현재 위치
    mid_dist = D
    for island in islands:
        if island - now >= mid:
            mid_dist = min(mid_dist, island-now)
            now = island
        else:
            cnt += 1
    mid_dist = min(mid_dist, D - now)

    if cnt > M:
        hi = mid-1
    else:
        # 최단 거리들 중 최대값
        answer = max(answer, mid_dist)
        lo = mid+1

print(answer)

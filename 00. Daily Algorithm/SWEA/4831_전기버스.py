import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    # 이동 거리, 최종 목표, 정류장 위치
    K, N, M = map(int, input().split())
    stations = set(map(int, input().split()))
    # 충전 횟수 버스 위치
    cnt = 0
    bus = 0

    print(stations)

    while bus < N:
        # 충전
        cnt = cnt + 1
        bus = bus + K

        # 도착
        if bus >= N:
            cnt = cnt - 1
            break

        for i in range(K):
            # 충전하고 전진
            if bus in stations:
                break
            # 충전소 만날때까지 후진
            bus = bus - 1
            # 도달할 수 없음
            if i == K-1:
                bus = N
                cnt = 0

    print(f'#{t}', cnt)

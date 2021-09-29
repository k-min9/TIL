'''
견적 : 
바이러스 선택 최대 경우의 수 10C5 = 252
최대 칸수 50 = 2500
2500 * 252 = 63만
완전 탐색에 계산 낭비 오케이
'''

import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

# 상수
MOVES = [(0, -1), (-1, 0), (0, 1), (1, 0)]

# 함수
def bfs():
    # 체크 값 (퍼뜨린 양)
    chk2 = 0
    dist = 0
    while que:    
        x, y = que.popleft()
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            # 그래프 안에 있고, 방문 안했고, 벽이 있고
            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == -1 and graphs[ny][nx] != 1:
                chk2 += 1
                visited[ny][nx] = visited[y][x] + 1
                # 비활성화 바이러스는 예외 (이거 한 줄 지우면 연구소 1)
                if graphs[ny][nx] == 0:
                    dist = max(dist, visited[ny][nx])
                que.append((nx, ny))               

    return chk2, dist


# 크기, 활성화 바이러스 개수
N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

# 선행, 공통 정보 정리. 칸 수 체크용 벽의 개수
chk = 0
viruses = list()
for y in range(N):
    for x in range(N):
        if graphs[y][x] == 2:
            viruses.append((x, y))
        if graphs[y][x] == 1:
            chk += 1

answer = 2500
for virus in combinations(viruses, M):
    visited = [[-1] * N for _ in range(N)]
    for x, y in virus:
        visited[y][x] = 0
    que = deque(virus)
    chk2, dist = bfs()
    if M + chk + chk2 == N**2:
        answer = min(answer, dist)

if answer != 2500:
    print(answer)
else:
    print(-1)

'''
활성화 바이러스가 비활성화 바이러스 만나서 변이 같은거 생겼으면 지옥이었다...
>> 비활성화 바이러스 만나면 복제가 필요 없으니 1초가 소모되지 않는다
>> 가 아니라 1초 소모되는데 마지막이 바이러스면 애초에 퍼뜨릴 필요 없으니 거기서 종료 한거임
오답이 너무 많이 나와서 지쳤,,,,
'''
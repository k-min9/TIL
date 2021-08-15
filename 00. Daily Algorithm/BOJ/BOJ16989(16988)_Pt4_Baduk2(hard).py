import sys
from collections import deque, defaultdict
input = sys.stdin.readline

# 덩어리 찾기용 상수
moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(i, j):
    visited[i][j] = 1
    # 2의 그룹과 2 주위 0의 그룹(집합)
    group_two = [(i, j)]
    group_zero = set()

    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for move in moves:
            nx = x + move[0]
            ny = y + move[1]
            if 1<=nx<=N and 1<=ny<=M:  # M과 N 순서 주의
                # 이어지는 내용물
                if maps[nx][ny] == 2 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    group_two.append((nx, ny))
                # 내용물 근처 0 기록(겹쳐도 오케이)
                if maps[nx][ny] == 0:
                    group_zero.add((nx, ny))
    # 타입: 리스트와 세트
    return group_two, sorted(list(group_zero))

# 입력
N, M = map(int, input().split())

# baduk2의 테두리 고려
maps = [[1 for _ in range(M+2)] for _ in range(N+2)]
for i in range(N):
    maps[i+1][1:M+1] = list(map(int, input().split()))

visited = [[0] *(M+2) for _ in range(N+2)]

# 돌 _n개로 스코어 획득 가능 점수 누적
dict_1 = defaultdict()
dict_2 = defaultdict()

for i in range(1, N+1):
    for j in range(1, M+1):
        # 방문 안한 테두리를 찾아서 BFS
        if not visited[i][j] and maps[i][j] == 2:
            # 2그룹, 0그룹
            group_two, group_zero = bfs(i, j)

            # 통으로 문자열 변환, 키로 써서 dic에 집어 넣는다.
            if len(group_zero) == 1:
                # 일타 쌍피의 가능성
                if str(group_zero) in dict_1.keys():
                    dict_1[str(group_zero)] += len(group_two)
                else:
                    dict_1[str(group_zero)] = len(group_two)

            elif len(group_zero) == 2:
                # 이타 쌍피의 가능성
                if str(group_zero) in dict_2.keys():
                    dict_2[str(group_zero)] += len(group_two)
                else:
                    dict_2[str(group_zero)] = len(group_two)

# 두 개 막았을때 한 개 짜리가 덤으로 따라올 수 있음. (이타 쌍피의 일타 버전)
# 키를 쪼갠다(물리)
for k in dict_2.keys():
    k1 = '[' + k[1:7] + ']'
    k2 = '[' + k[9:15] + ']'
    if k1 in dict_1.keys():
        dict_2[k] += dict_1[k1]
    if k2 in dict_1.keys():
        dict_2[k] += dict_1[k2]
            
# 애초에 죽일 수 있는 돌이 없음
if len(dict_1) == 0 and len(dict_2) == 0:
    print(0)
else:
    # 각각의 방법으로 죽일 수 있는 돌
    max_a = 0
    max_b = 0

    # 한 개의 돌로 죽일 수 있는 돌(2개 막기, 1개 막기, 없음)
    if len(dict_1) >= 2:
        max_a = sum(sorted(dict_1.values())[-2:])
    elif len(dict_1) == 1:
        max_a = list(dict_1.values())[0]

    # 두 개의 돌로 죽일 수 있는 돌
    if len(dict_2) >= 1:
        max_b = max(dict_2.values())

    print(max(max_a, max_b))

'''
BFS... set??
'''
import sys
input = sys.stdin.readline

# 상수
MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# 방 크기, 곰팡이 수, 검사(쿼리) 수, 남은 일 수
N, M, k, t = map(int, input().split())

visited = [[0]*N for _ in range(N)]
dirties = set()
for _ in range(M):
    x, y = map(int, input().split())
    dirties.add((x-1, y-1))
    visited[x-1][y-1] = 1
queries = list()
for _ in range(k):
    x, y = map(int, input().split())
    queries.append((x-1, y-1))

flag = False
answer = 'NO'
for time in range(t):
    tmp = set()  # 증식 곰팡이
    
    # 증식 곰팡이 확인
    for x, y in dirties:
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<N:
                visited[nx][ny] = 1
                tmp.add((nx, ny))
    
    # 쿼리 확인
    cnt = 0
    for x, y in queries:
        if (x, y) in tmp and (t-time+1)%2 == 0:
            answer = 'YES'
            break
        elif (x, y) not in tmp and visited[x][y]:
            cnt += 1
    else:
        if cnt == k:
            answer = 'NO'
            break
    if len(tmp) == 0:
        answer = 'NO'
        break

    # 다음 루프
    dirties = tmp

print(answer)

'''
오랜만에 시간 초과
>> visited 한 곳은 홀짝 체크하는 식으로 넘어가기
'''
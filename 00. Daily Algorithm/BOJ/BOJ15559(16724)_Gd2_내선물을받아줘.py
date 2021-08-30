'''
2차원 visited 아닌가
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 상수(y축 이동, x축 이동)
moves = {'N':(-1, 0), 'W':(0, -1), 'E':(0, 1), 'S':(1, 0)}

def dfs(y, x):
    global final_hit

    visited[y][x] = id
    stack.append((y,x))

    dy, dx = moves[maps[y][x]]
    nx = x + dx
    ny = y + dy
    if 0<=nx<M and 0<=ny<N:
        if not visited[ny][nx]:
            dfs(ny, nx)
        else:
            # 충돌시에만 기존 사이클과 충돌했는지 체크
            final_hit = visited[ny][nx]

N, M = map(int, input().split())

maps = [input().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]

answer = 0
for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            stack = list()
            answer = answer + 1
            id = answer
            final_hit = answer
            dfs(y, x)
            if final_hit != id:
                answer = answer - 1
                # 사이클 합류 = visited 갱신
                # 여기다가 sy, sx 같은 신 변수 안 넣고 y랑 x 넣고 왜 틀렸지 이러고 있었다. 바보.
                for sy, sx in stack:
                    visited[sy][sx] = final_hit

# for v in visited:
#     print(*v)
print(answer)

'''
풀다보면 눈치채는데 이거 SCC로 풀면 엄청 깔끔히 풀립니다. (몰라도 푸는데 지장 없음)
실제로 제 풀이가 id라던가 방향전환이 느껴지는 풀이
2차원이라 조금 이상하겠지만 Union-Find도 될거 같고 하여튼 사이클만 찾으면 뭐든지 오케이

16724 피리부는 사나이 moves = {'U':(-1, 0), 'L':(0, -1), 'R':(0, 1), 'D':(1, 0)} 만 바꾸면 완전히 같은 문제
'''
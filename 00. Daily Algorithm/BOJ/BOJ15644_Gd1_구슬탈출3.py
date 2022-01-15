'''
(13459, 13460, 15653) 구슬 탈출 1,2,4 => (15644) 구슬 탈출3 최종 문제
'''
import sys
from collections import deque
input = sys.stdin.readline


# 상수
MOVES = [(-1, 0, 'L'), (1, 0, 'R'), (0, 1, 'D'), (0, -1, 'U')]


def bfs(rx, ry, bx, by):
    que = deque()
    que.append((rx, ry, bx, by, ''))
    visited = set()
    visited.add((rx, ry, bx, by))

    count = 0  # 최대 시도 가능 횟수 : 10
    while que:
        # 카운트 기준
        for _ in range(len(que)):
            rx, ry, bx, by, history = que.popleft()
            if count > 10: 
                return -1
            if graphs[ry][rx] == 'O':
                return count, history
            for dx, dy, dir in MOVES:
                # 벽에 부딪힐때까지 이동 (R)
                nrx, nry = rx, ry
                while True:
                    nrx += dx
                    nry += dy
                    if graphs[nry][nrx] == '#':
                        nrx -= dx
                        nry -= dy
                        break
                    if graphs[nry][nrx] == 'O':
                        break
                # 벽에 부딪힐때까지 이동 (B)
                nbx, nby = bx, by
                while True:
                    nbx += dx
                    nby += dy
                    if graphs[nby][nbx] == '#':
                        nbx -= dx
                        nby -= dy
                        break
                    if graphs[nby][nbx] == 'O':
                        break
                # 애초에 파란 구슬이 들어가면 안됨                  
                if graphs[nby][nbx] == 'O':
                    continue      
                # 둘의 최종 위치가 같음 (먼 쪽이 한 칸 뒤로)
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx
                        nry -= dy
                    else:
                        nbx -= dx
                        nby -= dy
                # 방문 처리
                if (nrx, nry, nbx, nby) not in visited:
                    que.append((nrx, nry, nbx, nby, history + dir))
                    visited.add((nrx, nry, nbx, nby))
        count += 1
    return -1


# 입력
N, M = map(int, input().split())
graphs = list()
for y in range(N):
    graphs.append(list(input()))
    for x in range(M):
        if graphs[y][x] == 'R':
            ry, rx = y, x
        elif graphs[y][x] == 'B':
            by, bx = y, x

answer = bfs(rx, ry, bx, by)
if answer == -1:
    print(answer)
else:
    for ans in answer:
        print(ans)

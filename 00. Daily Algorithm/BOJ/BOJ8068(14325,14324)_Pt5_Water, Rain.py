'''
한 문제 풀면 네 개가 풀린다는 꿀 문제라는 제보
+ 심지어 메인 알고리즘이 BFS
이건 할 수 밖에 없다!
'''

import sys
input = sys.stdin.readline
from collections import deque


def BFS(x, y, height):

    global result
    q = deque()
    q.append([x,y])
    
    dx = (0,0,1,-1)
    dy = (1,-1,0,0)

    # 테두리에는 물이 고이지 않는다.
    border = False
    cnt = 1
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if not visited[nx][ny]:
                    if Rain[nx][ny] <= height:
                        q.append([nx,ny])
                        cnt+=1
                        visited[nx][ny] = True
            else:
                border = True
    if not border:
        result+=cnt
    return

for tc in range(int(input())):
    result = 0
    # 행, 열
    R, C = map(int,input().split())
    Rain = [list(map(int,input().split())) for _ in range(R)]
    # 수위를 올려가면서 BFS
    for height in range(1, 1000):
        visited = [[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if not visited[i][j] and Rain[i][j] <= height:
                    BFS(i, j, height)

    print(f'Case #{tc+1}:', result)
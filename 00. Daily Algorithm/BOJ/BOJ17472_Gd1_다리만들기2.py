'''
1. BFS 각각의 섬간의 거리 구하기
2. 다리 조건. 길이 2 이상, 방향 바뀌면 안됨, 연결 방향이 정상이어야함
3. 이후 MST로 가장 짧게

다리교차가능 ㄳㄳ
'''
from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visit = [[False]*m for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
land = dict()
landArr = []

# 섬 구분하여 좌표 구하기, BFS
landNum = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visit[i][j]:
            q = deque([(i,j)])
            visit[i][j] = True
            land[(i,j)] = landNum
            landArr.append((i,j,landNum))
            while q:
                x,y = q.popleft()
                for a,b in move:
                    dx=x+a; dy=y+b
                    if n>dx>=0 and m>dy>=0 and not visit[dx][dy] and board[dx][dy]:
                        q.append((dx,dy))
                        visit[dx][dy] = True
                        land[(dx,dy)] = landNum
                        landArr.append((dx,dy,landNum))
            landNum += 1

# 다리 제작
edges = []
for x,y,curLand in landArr:
    for a,b in move:
        dist = 0
        dx=x+a; dy=y+b
        while True:
            if n>dx>=0 and m>dy>=0:
                toLand = land.get((dx,dy))
                # 같은 섬
                if curLand==toLand:
                    break
                # 바다 위, 다리 길이 +1
                if toLand == None:
                    dx+=a; dy+=b
                    dist+=1
                    continue
                # 다리가 짧음
                if dist < 2:
                    break
                edges.append((dist,curLand,toLand))
                break
            else:
                break
edges = sorted(edges,reverse=True)

# 크루스칼 진행
def union(x,y):
    x = find(x)
    y = find(y)
    parents[y] = x

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

ans = 0
cnt = landNum-1
parents = [i for i in range(landNum)]
while cnt:
    try:
        w,a,b = edges.pop()
    except:
        # empty list, 다리 부족
        print(-1)
        sys.exit()
    if find(a) != find(b):
        union(a,b)
        ans += w
        cnt-=1
print(ans)

'''
리퍼런스가 워낙 많아서 오늘은 다른 분들의 코드를 보고 주석을 남기는 식으로 학습하였다.
PEP-8은 안맞지만 의식의 흐름상 가장 읽기 좋은 코드 였는듯
'''
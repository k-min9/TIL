'''
접근 : DFS - 우유 위치를 저장하고, 마셨는지 여부와 마실 수 있는지 여부를 체크하여 계산
'''
import sys
input = sys.stdin.readline

def dfs(x, y, hp, milk):
    global answer

    for mx, my in milks:
        if maps[mx][my] == 2:  # 현재까지 마시지 않은 우유인가
            dist = abs(x - mx) + abs(y - my)
            if dist <= hp:
                maps[mx][my] = 0
                dfs(mx, my, hp + H - dist, milk + 1)
                maps[mx][my] = 2
    
    if abs(x - hx) + abs(y - hy) <= hp:
        answer = max(answer, milk)

N, M, H = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 입력
# 우유들 위치와 초기 위치
milks = list()
hx, hy = 0, 0 

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            hx, hy = i, j
        if maps[i][j] == 2:
            milks.append((i, j))

answer = 0
dfs(hx, hy, M, 0)
print(answer)
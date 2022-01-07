'''
실제로 만들어보자 뿌요뿌요!
부수고 떨구고 부수고 떨구고! 더 이상 부술게 없을때까지
12*6 = 완!탐!
'''
from collections import deque
import sys
input = sys.stdin.readline


# 상수
MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(x, y, color):
    que = deque()
    que.append((x, y))

    delete_list = [(x, y)]

    visited = [[0]*6 for _ in range(12)]
    visited[y][x] = 1
    count = 1  # 4개 되면 폭팔

    while que:
        x, y = que.popleft()

        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if 0<=nx<6 and 0<=ny<12 and graphs[ny][nx] == color and not visited[ny][nx]:
                que.append((nx, ny))
                delete_list.append((nx, ny))
                visited[ny][nx] = 1
                count += 1
    
    if count >= 4:
        for x, y in delete_list:
            graphs[y][x] = '.'
        return 1  # 이번 루프 연쇄 있음
    return  # 일단 이건 연쇄 아님


def fall():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if graphs[j][i] != "." and graphs[k][i] == ".":
                    graphs[k][i] = graphs[j][i]
                    graphs[j][i] = "."
                    break


# 입력
graphs = [list(map(str, input().rstrip())) for _ in range(12)]


answer = 0
while True:
    # 이번 루프에서 종료 여부
    flag = 0
    visited = [[0]*6 for _ in range(12)]
    for y in range(12):
        for x in range(6):
            if graphs[y][x] != '.':
                if bfs(x, y, graphs[y][x]):
                    flag = 1

    if flag:
        answer += 1
    else:
        break
    fall()
print(answer)



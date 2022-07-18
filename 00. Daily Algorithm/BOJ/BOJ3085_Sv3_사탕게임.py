'''
보드 크기 50이라 N^4도 괜찮다는 기적의 브루트포스 풀이법...!

말고 없어요 진짜?
'''
import sys
input = sys.stdin.readline

# 상수
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 현재의 그래프에서 최대 사탕 수 계산
def count_candy():
    row_cnt, col_cnt, row_max, col_max = 1, 1, -1e9, -1e9
    # 행
    for x in range(N):
        for y in range(N-1):
            if board[x][y] == board[x][y+1]:
                row_cnt += 1
            else:
                row_cnt = 1
            row_max = max(row_cnt, row_max)
        row_cnt = 1

    # 열
    for y in range(N):
        for x in range(N-1):
            if board[x][y] == board[x+1][y]:
                col_cnt += 1
            else:
                col_cnt = 1
            col_max = max(col_cnt, col_max)
        col_cnt = 1

    return max(row_max, col_max)


answer = 0

N = int(input())
board = [list(input().strip()) for _ in range(N)]

for x in range(N):
    for y in range(N):
        for dx, dy in MOVES:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
                
            # 다를 때만 계산하지 뭐
            if board[x][y] != board[nx][ny]:
                board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
                answer = max(answer, count_candy())
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]

print(answer)

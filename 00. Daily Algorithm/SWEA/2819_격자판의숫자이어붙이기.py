import sys
sys.stdin = open('input.txt')

# 상수
MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dfs(x, y, s, length):
    if length == 7:
        answers.add(s)
        return

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <=nx< 4 and 0 <=ny< 4:
            dfs(nx, ny, s + graphs[nx][ny], length+1)


for tc in range(1, int(input()) + 1):
    graphs = [input().split() for _ in range(4)]
    answers = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, graphs[i][j], 1)

    print(f'#{tc}', len(answers))

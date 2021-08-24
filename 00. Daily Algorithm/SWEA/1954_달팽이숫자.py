import sys
sys.stdin = open('input.txt')


def snail(i, j, dir):

    x = i + moves[dir][0]
    y = j + moves[dir][1]
    if 0 <= x < N and 0 <= y < N and boxes[x][y]==0:
        pass
    else:
        dir = (dir + 1) % 4
        x = i + moves[dir][0]
        y = j + moves[dir][1]
    return x, y, dir


# 달팽이 이동 알고리즘
moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

T = int(input())
for t in range(T):
    N = int(input())

    boxes = [[0]*N for _ in range(N)]

    # 달팽이 초기 정보
    moves_dir = 0
    x = 0
    y = 0

    for i in range(N**2):
        boxes[x][y] = i + 1
        x, y, moves_dir = snail(x, y, moves_dir)

    print(f'#{t + 1}')
    for i in range(N):
        print(*boxes[i])


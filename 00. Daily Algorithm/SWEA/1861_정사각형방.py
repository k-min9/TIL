import sys
sys.stdin = open('input.txt')

#상수
MOVES = [(-1,0), (1, 0), (0, -1), (0, 1)]


for tc in range(int(input())):
    # 가로길이
    N = int(input())
    graphs = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N*N + 1)

    for x in range(N):
        for y in range(N):
            for dx, dy in MOVES:
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<N:
                    if graphs[ny][nx] == graphs[y][x] + 1:
                        visited[graphs[y][x]] = 1
                        break
    answer_start = 0
    answer_max = 0
    sums = 1
    for i in range(1, N*N+1):
        if visited[i]:
            sums += 1
            if sums > answer_max:
                answer_max = sums
                answer_start = i - answer_max + 2
        else:
            sums = 1

    print(f'#{tc+1}', answer_start, answer_max)

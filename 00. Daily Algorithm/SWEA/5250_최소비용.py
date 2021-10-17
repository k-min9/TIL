import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# 상수
MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))
INF = 987654321


def dijkstra(x, y):
    heap = []
    dists[x][y] = 0
    heappush(heap, (0, 0, 0))
    while heap:
        cur_dist, x, y = heappop(heap)
        for dx, dy in MOVES:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = max(0, matrix[nx][ny] - matrix[x][y]) + 1
                next_dist = cur_dist + cost
                if dists[nx][ny] > next_dist:
                    dists[nx][ny] = next_dist
                    heappush(heap, (next_dist, nx, ny))


for tc in range(int(input())):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dists = [[INF] * N for _ in range(N)]

    dijkstra(0, 0)

    print(f'#{tc+1}', dists[N - 1][N - 1])

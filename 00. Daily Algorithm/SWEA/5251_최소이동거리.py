import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

# 상수
MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))
INF = 987654321


def dijkstra(start):
    heap = list()
    heappush(heap, [0, start])

    while heap:
        w, x = heappop(heap)
        for nx, nw in graph[x]:
            tmp = w + nw

            if tmp < dists[nx]:
                dists[nx] = tmp
                heappush(heap, [tmp, nx])


for tc in range(int(input())):
    # 이동 지점, 구간 갯수
    N, E = map(int, input().split())

    graph = [[] for _ in range(E+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    dists = [INF] * (E + 1)
    dijkstra(0)

    print(f'#{tc+1}', dists[N])

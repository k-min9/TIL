'''
간선이 이어져서 통과 가능해진 시점이 언제냐는 질문
ㄴ 다익스트라의 거리가 이어진 시점 ㄷㄷㄷ
'''
import heapq
import sys
input = sys.stdin.readline


# 상수
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dis[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if dis[now] < d:
            continue
        for v, w in graph[now]:
            cost = d + w
            if cost < dis[v]:
                dis[v] = cost
                heapq.heappush(q, (cost, v))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [INF]*(N+1)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
s, t = map(int, input().split())
dijkstra(s)
print(dis[t])
'''
이동에 가장 많은 시간을 소비하는 학생 찾기
단방향이라 다익스트라 이동을 두 번 해야함
'''
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

def dijkstra(start):
    q = []
    distance = [INF] * (v + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for node_index, node_cost in graph[now]:
            cost = dist + node_cost

            if distance[node_index] > cost:
                distance[node_index] = cost
                heapq.heappush(q, (cost, node_index))

    return distance

v, e, x = map(int, input().split())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


result = 0
for i in range(1, v + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)

'''
시작점과 끝점 도착 전에 두 군데를 들려야 함
다익스트라 돌려서
시작 -> 1 -> 2 -> 끝점
시작 -> 2 -> 1 -> 끝점
을 각각 더해서 작은걸 쓰면 끝남
'''
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (v + 1)
    queue = list()
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

    return distance

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]

# 무방향성
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

v1, v2 = map(int, input().split())

dist_from_start = dijkstra(1)
dist_form_node1 = dijkstra(v1)
dist_from_node2 = dijkstra(v2)

answer1 = dist_from_start[v1] + dist_form_node1[v2] + dist_from_node2[v]
answer2 = dist_from_start[v2] + dist_from_node2[v1] + dist_form_node1[v]

answer = min(answer1, answer2)
if answer < INF:
    print(answer)
else:
    print(-1)

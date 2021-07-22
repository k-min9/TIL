'''
그래프가 주어진 BFS
'''

import sys
input = sys.stdin.readline

from collections import deque

N , M = map(int, input().split())

#BFS용 초기화
graph = [[] for _ in range(N + 1)]
dist = [0] * (N + 1)

#트리(그래프) 간선 입력
for _ in range(M):
    nodeA, nodeB = map(int, input().split())
    graph[nodeA].append(nodeB) #방향성 없음
    graph[nodeB].append(nodeA) #방향성 없음

#BFS
def bfs():
    q = deque([1])
    dist[1] = 1 # visited 역할 수행하는 대신에 모든 값이 1 증가한다.
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not dist[next]:
                dist[next] = dist[now] + 1
                q.append(next)

#실행
bfs()
distance = max(dist)

print(dist.index(distance), distance - 1, dist.count(distance))

'''
find : 없는 경우 -1 출력
index : 리스트, 듀플, 딕셔너리는 index!
'''
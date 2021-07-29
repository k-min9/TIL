'''
정점이라길래 예시 최고 노드가 5개 라는 줄 알았네;; 노드 얘기

- 트리의 지름 구하는 법 -
1. 아무 노드나 하나 찍는다.
2. 1의 노드에서 가장 먼 노드를 하나 찍는다
3. 2의 노드에서 가장 먼 노드를 찍는다.
2의 노드와 3의 노드의 거리가 트리의 지름이다
'''

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

# 1167 Gd3
# for _ in range(N):
#     graph_info = list(map(int, input().split()))
#     for i in range(1,len(graph_info)-1,2):
#         # 양방향이지만 반대 노드도 적힌 예시를 주기 때문에 한번만 써도 됨
#         graph[graph_info[0]].append((graph_info[i], graph_info[i+1]))  # 기준노드, 연결노드, 노드 거리

# 1967 Gd4
for _ in range(N-1):
    graph_info = list(map(int, input().split()))
    graph[graph_info[0]].append((graph_info[1], graph_info[2]))  # 기준노드, 연결노드, 노드 거리
    graph[graph_info[1]].append((graph_info[0], graph_info[2]))

# 리팩토링 없이 직접 좀 해봤다.
def bfs(start):
    visited = [0] * (N+1)
    distance = [0] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 1

    far_max = [0,0]  # 노드, 거리 기록

    while q:
        x = q.popleft()
        for next, dist in graph[x]:
            if not visited[next]:
                distance[next] = distance[x] + dist
                visited[next] = 1
                q.append(next)
                if far_max[1] < distance[next]:
                    far_max[1] = distance[next]
                    far_max[0] = next
    return far_max

print(bfs(bfs(1)[0])[1])

'''
bfs 반성점. 평소에는 visited 안썼네 나. distance 하나로 다 해결 가능 했음
'''
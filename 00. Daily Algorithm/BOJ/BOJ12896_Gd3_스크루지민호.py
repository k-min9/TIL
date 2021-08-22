'''
첫번째 접근 : 각 정점마다 가장 먼 거리 하나씩 뽑아서 그거 min 하면 시간 맞으려나
N = 10만 > 네 시간 초과
두번째 접근 :  간선 거리가 1이면 트리의 지름 구한거 /2하면 끝아님?
'''

import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited = [0] * (N+1)
    distance = [0] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = 1

    # 노드, 거리 기록
    far_max = [0,0]  

    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visited[next]:
                distance[next] = distance[x] + 1
                visited[next] = 1
                q.append(next)
                if far_max[1] < distance[next]:
                    far_max[1] = distance[next]
                    far_max[0] = next
    return far_max

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# answer = N+1
# for i in range(1, N+1):
#     answer = min(answer, bfs(i))

print((bfs(bfs(1)[0])[1] + 1)//2)

'''
이게 되네
'''
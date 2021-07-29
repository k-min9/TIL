'''
from BOJ1167(1967)_Gd3_트리의_지름
보는 순간 촉이 왔다. a와 b가 지름을 만든다면,
두 번째 지름은 노드 한 쪽에, 적어도 a 또는 b가 들어가게 되어있다. 
쌍견제는 불가능함. ...아님 말고
'''

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    graph_info = list(map(int, input().split()))
    graph[graph_info[0]].append((graph_info[1], graph_info[2]))  # 기준노드, 연결노드, 노드 거리
    graph[graph_info[1]].append((graph_info[0], graph_info[2]))

# block 추가
def bfs(start, block = 0):
    visited = [0] * (N+1)
    visited[block] = 1  # 두 번째 트리의 지름을 위해서 통제

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

nodeA = bfs(1)[0]
nodeB = bfs(nodeA)[0]

print(max(bfs(nodeA,nodeB)[1], bfs(nodeB,nodeA)[1]))


'''
생각한데로 일이 진행되면 기분이 진짜 좋지
'''
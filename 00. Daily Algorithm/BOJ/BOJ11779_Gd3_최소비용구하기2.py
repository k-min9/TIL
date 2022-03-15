'''
무지성 다익스트라
'''
import sys
input = sys.stdin.readline
from heapq import heappop, heappush


# 상수
INF = 1e9

def dijkstra(start, end):

    distance = [INF] * (N+1) #start 노드로부터 최단거리테이블 초기화
    answers = [[] for _ in range(N + 1)]  # 경로 저장용
    answers[start] = [start]
    
    q = []
    heappush(q, [0, start]) # distance, idx
    distance[start] = 0 #출발이니 0

    while q: #큐가 비어있지 않다면
        #가장 가까운 최단거리 노드 정보 pop
        dist, nodeClose = heappop(q)
        #이미 처리 되었을 경우 다음 루프
        if distance[nodeClose] < dist:
            continue
        #현재 노드와 연결된 다른 노드 확인
        for next_dist, next_node in graph[nodeClose]:  # 이 부분 개선 b
            cost = dist + next_dist # 현 시점에서 dist = distance[nodeClose]
            #현재 노드를 거치는게 더 짧을 경우 갱신
            if cost < distance[next_node]:
                distance[next_node] = cost
                heappush(q, [cost, next_node])
                answers[next_node] = answers[nodeClose] + [next_node]

    return distance, answers[end] #최단 거리 테이블 반환


N = int(input()) # 도시
M = int(input()) # 간선
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    nodeA, nodeB, dist = map(int,input().split())
    graph[nodeA].append((dist,nodeB)) # treeA에서 treeB까지의 거리 dist (미방향 노드)

# 출발, 도착
s, e = map(int, input().split())

#함수 실행

answer, answers = dijkstra(s, e)

print(answer[e])
print(len(answers))
print(*answers)
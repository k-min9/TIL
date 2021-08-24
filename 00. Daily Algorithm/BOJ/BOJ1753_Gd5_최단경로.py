'''
무지성 다익스트라 문제
'''

# 전처리
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 자료 구조 버전
def dijkstra(nodeStart):

    INF = 1e9 #무한을 대체할 값
    distance = [INF] * (N+1) #start 노드로부터 최단거리테이블 초기화
    
    q = []
    heappush(q, [0, nodeStart]) # distance, idx
    distance[nodeStart] = 0 #출발이니 0

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

    return distance #최단 거리 테이블 반환


#노드의 개수, 간선의 개수
N, M = map(int, input().split())

# 시작 정점
start = int(input())

#트리(그래프) 정보 입력용 리스트
graph = [[] for _ in range(N + 1)]

#간선의 개수(M) 만큼 정보 입력
for _ in range(M):
    nodeA, nodeB, dist = map(int,input().split())
    graph[nodeA].append((dist,nodeB)) # treeA에서 treeB까지의 거리 dist (미방향 노드)

#함수 실행
answer = dijkstra(start)

for i in range(1,N+1):
    if answer[i] != 1e9:
        print(answer[i])
    else:
        print('INF')
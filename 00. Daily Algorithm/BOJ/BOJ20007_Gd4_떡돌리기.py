'''
한 집에서 모든 집까지의 최소거리 전부 구하기 << 다익스트라

다익스트라 복습
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3, 4 반복
'''

# 전처리
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

# 자료 구조 버전
def dijkstra(nodeStart):

    INF = 1e9 #무한을 대체할 값
    distance = [INF] * N #start 노드로부터 최단거리테이블 초기화
    q = []
    heappush(q, [0, nodeStart]) # distance, idx
    distance[nodeStart] = 0 #출발이니 0
    while q: #큐가 비어있지 않다면
        #가장 가까운 최단거리 노드 정보 pop
        dist, nodeClose = heappop(q)
        #이미 처리 되었을 경우 다음 루프
        if distance[nodeClose] < dist:
            continue
        #visited[nodeClose] = 1
        #현재 노드와 연결된 다른 노드 확인
        for i in graph[nodeClose]:
            cost = dist+ i[1] # 현 시점에서 dist = distance[nodeClose]
            #현재 노드를 거치는게 더 짧을 경우 갱신
            if cost < distance[i[0]]:# and not visited[i[0]]:
                distance[i[0]] = cost
                heappush(q, [cost, i[0]])
    return distance #최단 거리 테이블 반환


#노드의 개수, 간선의 개수, 최대 이동, 스타트 위치
N, M, X, Y = map(int, input().split())

#트리(그래프) 정보 입력용 리스트
graph = [[] for _ in range(M + 1)]

#간선의 개수(M) 만큼 정보 입력
for _ in range(M):
    nodeA, nodeB, dist = map(int,input().split())
    graph[nodeA].append((nodeB,dist)) # treeA에서 treeB까지의 거리 dist (미방향 노드)
    graph[nodeB].append((nodeA,dist)) # treeB에서 treeA까지의 거리 dist (미방향 노드)

#함수 실행
distance = dijkstra(Y)

#print(distance)
#답안 작성
#2배수 이상 못가거나 노드가 연결되어있지 않음
if X < 2 * max(distance):
    print(-1)
else:
    # 밑에서 긁어가면서 조합해보기
    answer = 1
    energy = X
    distance.sort()
    while(distance):
        d = 2 * heappop(distance)
        if energy >= d:
            energy = energy - d
        else:
            answer = answer + 1
            energy = X - d
    print(answer)
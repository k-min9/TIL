'''
키워드 체크 : 트리, DFS, BFS
접근 : 문제 이해하는데 한 참 걸렸다.
다익스트라 최단 경로 알고리즘 연습 문제로 풀어보자.
공부 : https://www.youtube.com/watch?v=acqm9mM1P6o&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=7
'''

'''
다익스트라
1. 출발 노드 설정
2. 최단 거리 테이블 초기화
3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
5. 3, 4 반복
'''

# 0 인풋, 트리 정리 및 초기화
import sys
input = sys.stdin.readline
INF = int(10000000) #무한을 대체할 값 16384(최대치 10000)

import heapq # 자료구조 최소heap 투입

#노드의 개수, 풀어야할 문제수
N, M = map(int, input().split())

#트리(그래프) 정보 입력용 리스트
graph = [[] for i in range(N + 1)]

#간선의 개수(N-1) 만큼 정보 입력
for _ in range(N - 1):
    nodeA, nodeB, dist = map(int,input().split())
    graph[nodeA].append((nodeB,dist)) # treeA에서 treeB까지의 거리 dist (미방향 노드)
    graph[nodeB].append((nodeA,dist)) # treeB에서 treeA까지의 거리 dist (미방향 노드)

'''1차 버전
visited = [0] * (N + 1) #방문 정보 입력용 리스트, False
distance = [INF] * (N + 1) #start 노드로부터 최단거리테이블 초기화


#미방문 노드 중에서 가장 최단거리가 짧은 노드를 반환
def get_closest_node():
    min_value = INF
    index = 0 
    for i in range(1, N + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i # 가장 최단 거리가 짧은 노드의 인덱스
    return index


def dijkstra(nodeStart):

    #초기정보(본인)
    distance[nodeStart] = 0
    visited[nodeStart] = True #0->1
    for i in graph[nodeStart]:
        distance[i[0]] = i[1]
    
    #자신을 제외한 모든 미방문 노드(N-1개)에 방문
    for i in range(N - 1):
        #모든 노드 중 가장 짧은 노드를 방문처리
        nodeClose = get_closest_node()
        visited[nodeClose] = True
        #현재 노드와 연결된 다른 노드를 확인
        for j in graph[nodeClose]:
            cost = distance[nodeClose] + j[1]
            #현재 노드를 거치는게 더 짧을 경우 갱신
            if cost < distance[j[0]]:
                distance[j[0]] = cost
'''

# 자료 구조 버전
def dijkstra(nodeStart, nodeEnd):

    #visited = [0] * (N + 1) #방문 정보 입력용 리스트, False
    distance = [INF] * (N + 1) #start 노드로부터 최단거리테이블 초기화
    que = []
    heapq.heappush(que, (0, nodeStart))
    distance[nodeStart] = 0
    while que: #큐가 비어있지 않다면
        #가장 가까운 최단거리 노드 정보 pop
        dist, nodeClose = heapq.heappop(que)
        #이미 처리 되었을 경우 다음 루프
        if distance[nodeClose] < dist:# or visited[nodeClose]:
            continue
        #visited[nodeClose] = 1
        #현재 노드와 연결된 다른 노드 확인
        for i in graph[nodeClose]:
            cost = dist+ i[1] # 현 시점에서 dist = distance[nodeClose]
            #현재 노드를 거치는게 더 짧을 경우 갱신
            if cost < distance[i[0]]:# and not visited[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(que, (cost, i[0]))

    print(distance[nodeEnd])    

#답안 작성

for _ in range(M):
    start, end = map(int,input().split())
    dijkstra(start, end)

'''
1차 결과 : 시간 초과 >>> 죄다 주석 처리
자료구조 투입 : 최소 heap
'''

'''
2차 결과 : 계속 틀리길래
INF를 16384에서 10000000으로 고쳐줬더니 풀렸다...
'''

'''
3차 결과 : visit 없이도 돌아간다. 조금 빨라졌지만 DFS보다 훨씬 느려보인다.
'''
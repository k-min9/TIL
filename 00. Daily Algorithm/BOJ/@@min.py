'''
시험전 이거는 보고 가야한다 목록 만들어두자
'''
from collections import deque
from heapq import heappop, heappush, heapify

# 2차원 배열을 1차원 배열로(파이써닉)
import itertools
a = [[1,2,3],[4,5,6],[7,8,9]]
b = [j for i in a for j in i]
c = list(itertools.chain(*a))


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


def floid(maps, i, j, k):
    # 경유지, 목적지, 기본 이동 코스
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]

def bellmanFord(N, graph, dp, INF):
    global isPossible
    
    for repeat in range(N):
        for i in range(1, N + 1):
            for next, dist in graph[i]:
                if dp[i] != INF and dp[next] > dp[i] + dist:
                    dp[next] = dp[i] + dist
                    # 음의 싸이클 체크 = N-1바퀴 돌아도 갱신중
                    if repeat == N - 1:
                        isPossible = False


def union(a, b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a] = b
    else:
        parent[b] = a

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

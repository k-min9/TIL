'''
N = 200 / 플로이드 와샬, 다익스트라 N회 전부 상관 없음
'''
from heapq import heappop, heappush

# 풀이 1 : 다익스트라

# 상수
INF = 1e9

def solution(n, s, a, b, fares):
    #노드수, 스타드 노드, 도착A, 도착B, 요금표
    
    def dijkstra(nodeStart, nodeEnd):
        distance = [INF] * (n+1)
        distance[nodeStart] = 0
        q = [[0, nodeStart]]
        
        while q:
            dist, cur = heappop(q)
            if distance[cur] < dist:
                continue
            for dist_next, next in graphs[cur]:
                cost = dist + dist_next
                if cost < distance[next]:
                    distance[next] = cost
                    heappush(q, [cost, next])

        return distance[nodeEnd]

    graphs = [[] for _ in range(n+1)]
    for nodeA,nodeB,w in fares:
        graphs[nodeA].append((w,nodeB))
        graphs[nodeB].append((w,nodeA))
    
    answer = INF
    for i in range(1, n+1):
        answer = min(answer, dijkstra(s,i)+dijkstra(i,a)+dijkstra(i,b))

    return answer 

'''
graphs = [[] for _ in range(n+1)]
for a,b,w in fares:
    graphs[a].append((w,b))
    graphs[b].append((w,a))

얘가 대형사고 발생시킴. 자세한 설명은 생략한다.

'''

# 풀이 2 : 플로이드 와샬

def solution(n, s, a, b, fares):
    dist = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        dist[i][i] = 0

    for u,w,c in fares:
        dist[u][w] = c
        dist[w][u] = c

    
    for m in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                val = dist[i][m] + dist[m][j]
                if val < dist[i][j]:
                    dist[i][j] = val
                    
    answer = INF
    for m in range(1,n+1):
        answer = min(answer, dist[s][m] + dist[m][a] + dist[m][b])

    return answer


# answer : 82
print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))


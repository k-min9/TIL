# https://leetcode.com/problems/network-delay-time/
# 풀이 : 다익스트라 + 딕셔너리???

import collections
import heapq

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    # 입력
    graph = collections.defaultdict(list)
    for u,v,w in times:
        graph[u].append((v,w))
        
    # 출발노드(K) 설정
    Q = [(0, k)]
    dist = collections.defaultdict(int)
    
    # 우선순위 큐 ㄱㄱ
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
                
    print(dist)
    if len(dist) == n:
        return(max(dist.values()))
    return -1

networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
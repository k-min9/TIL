'''
1197, 1922의 최소 신장 트리 만들기는 크루스칼 썼고, 이번 문제는 프림을 써보고자 한다. 
프림 : 시작점을 정하고, 시작점에서 가까운 정점을 선택하면서 트리르 구성
자세한 설명은 1197쪽에 기술
'''

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def prim(node):
    q = []
    tree[node] = 1
    # sum(tree)하지 않고 카운트
    cnt = 1

    # 트리 간선 값, 도시 분리용 댓가
    result = 0
    max_weight = 0

    # 인접노드 최소 큐에 넣기
    for i in graph[node]:
        heappush(q, i)

    while q:
        weight, node = heappop(q)
        # 첫 방문 체크
        if not tree[node]:
            tree[node] = 1
            cnt = cnt + 1
            result += weight
            # 마을 나누기
            max_weight = max(max_weight, weight)
            # 인접노드 최소 큐에 넣기
            for i in graph[node]:
                heappush(q, i)
        if cnt == N:
            return result - max_weight

# 계산 시작
N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
tree = [0] * (N+1)

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((w, b))
    graph[b].append((w, a))

print(prim(1))

'''
프림쪽이 압도적으로 편하다!
'''
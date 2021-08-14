'''
1647에서 프림 참조, 개량
'''

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def prim(node):
    q = []
    tree[node] = 1
    # sum(tree)하지 않고 카운트
    cnt = 1
    # 정답 적기
    answers = []

    # 인접노드 최소 큐에 넣기
    for i in graph[node]:
        heappush(q, i)

    while q:
        weight, node_b, node_a = heappop(q)
        bounds[node_a-1] = bounds[node_a-1] - 1
        bounds[node_b-1] = bounds[node_b-1] - 1
        if bounds[node_a-1] < 0 or bounds[node_b-1] < 0:
            bounds[node_a-1] = bounds[node_a-1] + 1
            bounds[node_b-1] = bounds[node_b-1] + 1
            continue
        # 첫 방문 체크
        if not tree[node_b]:
            tree[node_b] = 1
            answers.append((node_a, node_b))
            cnt = cnt + 1
            # 인접노드 최소 큐에 넣기
            for i in graph[node_b]:
                heappush(q, i)
        else:
            bounds[node_a-1] = bounds[node_a-1] + 1
            bounds[node_b-1] = bounds[node_b-1] + 1

        # 종료    
        if cnt == N:
            return answers
    return 'NO'

# 계산 시작
N, M = map(int,input().split())
bounds = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
tree = [0] * (N+1)

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((w, b, a))
    graph[b].append((w, a, b))

answers = prim(1)

if answers == 'NO':
    print(answers)
else:
    print('YES')
    for answer in answers:
        print(answer[0], answer[1])

'''
브루트 포스 + 백트래킹이라고 한다. 나는 돌아올 것이다.
'''
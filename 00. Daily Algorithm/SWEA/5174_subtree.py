# 위상정렬
import sys
sys.stdin = open('input.txt')
from collections import deque

for t in range(int(input())):
    # 간선 수, 쿼리
    E, N = map(int, input().split())

    # 그래프(노드 수 = 간선 수 + 1)
    graphs = [[] for _ in range(E+2)]
    indegree = [0] * (E+2)

    edges = list(map(int, input().split()))
    for i in range(E):
        a, b = edges[2*i], edges[2*i+1]
        graphs[b].append(a) # 자식 -> 부모만 있으면 됨
        indegree[a] = indegree[a] + 1

    # 큐 세팅
    que = deque()
    for i in range(1, E+2):
        if indegree[i] == 0:
            que.append(i)

    # 엔딩
    answers = [0]*(E+2)
    while que:
        q = que.popleft()
        answers[q] = answers[q]+1
        for i in graphs[q]:
            indegree[i] -= 1
            answers[i] += answers[q]
            if indegree[i] == 0:
                que.append(i)

    print(f'#{t+1}', answers[N])

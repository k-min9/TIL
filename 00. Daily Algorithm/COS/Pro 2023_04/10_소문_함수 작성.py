'''
BFS
'''
from collections import deque

def solution(n, k, acquaintance):
    def bfs(start):
        q = deque([start])
        while q:
            cur = q.popleft()
            for next in graphs[cur]:
                if dists[next] == -1:
                    dists[next] = dists[cur] + 1
                    q.append(next)

    graphs = [[] for _ in range(n+1)]
    for s, e in acquaintance:
        graphs[s].append(e)
        graphs[e].append(s)

    dists = [-1]*(n+1)
    dists[1] = 0

    bfs(1)
    print(graphs)
    print(dists)

    return dists[k]

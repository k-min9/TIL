# starts를 구하고, 각각의 starts에서 말단까지
from collections import deque

def solution(n, roads):
    def bfs(start):
        dist = []
        visited = [0] * (n+1)
        queue = deque([[start, list()]])
        visited[start] = 1

        while queue:
            node_cur, costs = queue.popleft()
            for node_next, cost in graphs[node_cur]:
                if not visited[node_next]:
                    visited[node_next] = 1
                    if node_next in ends:
                        dist.append(costs+[cost])
                    else:
                        queue.append([node_next, costs+[cost]])

        return dist[0][0]


    graphs = [[] for _ in range(n+1)]
    starts = set()
    ends = set()
    max_len = 0
    for a, b, cost in roads:
        graphs[a].append([b,cost])
        graphs[b].append([a,cost])
        if cost > max_len:
            max_len = cost
            starts = {a, b}
        elif cost == max_len:
            starts.add(a)
            starts.add(b)

    for i in range(1, n+1):
        if len(graphs[i]) == 1:
            ends.add(i)

    for start in starts:
        max_len = min(max_len, bfs(start))

    return max_len
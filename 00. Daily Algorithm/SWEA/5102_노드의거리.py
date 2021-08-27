import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(start):

    q = deque()
    q.append(start)
    visited = [0] * (V+1)
    visited[start] = 1

    while q:
        x = q.popleft()
        for next in graph[x]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[x] + 1

    return visited


# 시작
T = int(input())
for t in range(T):
    # 노드 간선
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        S, G = map(int, input().split())
        # 무방향성 간선
        graph[S].append(G)
        graph[G].append(S)

    # 풀이 시작
    start, goal = map(int, input().split())
    answers = bfs(start)

    print(f'#{t + 1}', max(answers[goal] - 1, 0))


import sys
sys.stdin = open('input.txt')

# 시작
T = int(input())
for t in range(T):
    # 노드 간선
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        S, G = map(int, input().split())
        # 방향성 간선
        graph[S].append(G)

    # 풀이 시작
    start, goal = map(int, input().split())
    stack = list()
    visited = set()
    stack.append(start)
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        stack.extend(graph[cur])

    if goal in visited:
        print(f'#{t + 1}', 1)
    else:
        print(f'#{t + 1}', 0)

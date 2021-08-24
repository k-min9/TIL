import sys
sys.stdin = open('input.txt')

# 시작

for _ in range(10):
    t, N = map(int, input().split())
    graph = [[] for _ in range(100)]
    infos = list(map(int,input().split()))
    for i in range(N):
        graph[infos[2*i]].append(infos[2*i+1])

    # 풀이 시작(출발 0, 골 99)
    stack = list()
    visited = set()
    stack.append(0)
    while stack:
        cur = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        stack.extend(graph[cur])

    if 99 in visited:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)

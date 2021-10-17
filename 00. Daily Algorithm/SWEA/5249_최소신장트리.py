import sys
sys.stdin = open('input.txt')


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b


for tc in range(int(input())):
    V, E = map(int, input().split())
    parents = list(range(V+1))
    edges = list()
    for __ in range(E):
        a, b, w = map(int, input().split())
        edges.append((w, a, b))

    edges.sort()

    answer = 0
    for w, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            answer += w

    print(f'#{tc+1}', answer)

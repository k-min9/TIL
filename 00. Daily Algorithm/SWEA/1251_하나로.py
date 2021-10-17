import sys
sys.stdin = open('input.txt')
from heapq import heappop, heappush


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x
    parents[y] = x


for tc in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    parents = {i: i for i in range(N)}
    E = float(input())
    edges = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            heappush(edges, (abs(X[i] - X[j])**2 + abs(Y[i] - Y[j])**2, i, j))

    answer = 0
    cnt = 0
    while edges:
        dists, a, b = heappop(edges)
        if find(a) != find(b):
            union(a, b)
            answer += E * dists
            cnt += 1
        if cnt == N - 1:
            break

    print(f'#{tc+1}', round(answer))

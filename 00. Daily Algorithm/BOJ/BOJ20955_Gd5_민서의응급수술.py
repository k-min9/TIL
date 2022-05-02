'''
트리가 되기 위해 필요한 연결 횟수 = Union - find
'''
import sys
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if b<a:
        parent[a] = b
    else:
        parent[b] = a

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


# 뉴런의 개수, 시냅스의 개수
N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
parent = list(range(N+1))

answer = 0
for _ in range(M):
    a, b = map(int, input().split())
    # 이미 같음 = 사이클 = 끊어야함
    if find(a) == find(b):
        answer += 1
    union(a, b)

# 이제부터 연결
for i in range(1, N):
    if find(i) != find(i+1):
        union(i, i+1)
        answer += 1

print(answer)

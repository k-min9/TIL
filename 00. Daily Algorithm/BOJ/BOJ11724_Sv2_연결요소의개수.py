'''
Union find로 좀 쎄게
'''
import sys
input = sys.stdin.readline

# 지원함수 1 : 유니온 - 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 갱신 내지 재정의
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

# 지원함수 2 : find - 루트 노드를 찾을때까지 재귀적으로 반환
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


# 서로소 집합 자료구조용 입력 정보
N, M = map(int, input().split())
parent = list(range(N+1))
graphs = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

for a in range(1, N+1):
    for b in graphs[a]:
        union(a, b)

results = set()
for i in range(1, N+1):
    results.add(parent[i])
print(len(results))

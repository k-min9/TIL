'''
최소 스패닝 트리 요즘 잦네
+ i*T 빼고 정석적
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

N, M, T = map(int, input().split())
parent = list(range(N+1))
edges = list()

for i in range(M):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))

edges.sort()

answer = 0
i = 0
# 간선을 하나씩 확인
for weight, start, end in edges:
    # 루트가 같음 = 사이클 = 잇지 않는다.
    if find(start) != find(end):
        union(start, end)
        answer += weight + i * T
        i += 1

print(answer)

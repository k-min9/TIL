'''
최소 스패닝 트리 with 크루스칼
'''
import sys
input = sys.stdin.readline


# 유니온 - 파인드로 사이클 확인
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


N, M = map(int, input().split())
sex = input().strip().split(' ')

# 서로소 집합 자료구조용 입력 정보
parent = list(range(N+1))

# 간선 정보 정리
edge = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edge.append((u, v, w))

# 애초에 w 앞에 둘 걸
edge = sorted(edge, key=lambda x: x[2])
answer = 0
count = 0

for u, v, w in edge:
    # 루트가 같음 = 사이클 = 잇지 않는다. 성별이 달라야한다.
    if find(u) != find(v) and sex[u-1] != sex[v-1]:
        union(u, v)
        answer += w
        count += 1
    if count == N-1:
        break
if count != N-1:
    answer = -1
print(answer)
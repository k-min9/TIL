'''
크루스칼 알고리즘(최소 신장 트리 알고리즘, 그리디)
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
1) 발생하지 않는 경우, 최소 신장트리에 포함
2) 발생하는 경우, 포함되지 않음
'''

import sys
input = sys.stdin.readline

# 서로소 집합 자료구조 (합치기 찾기 자료구조)
# 사이클 여부를 확인하는 크루스칼의 핵심 부분

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

# 정점 수, 간선 수
V, E = map(int, input().split())

# 서로소 집합 자료구조용 입력 정보
parent = list(range(V+1))

# 간선 정보 정리
edges = []
for _ in range(E):
    a, b, w = map(int, input().split())
    edges.append((w, a, b))  # 무 방향이지만 아마 이번 문제는 하나만 추가해도 될 것
    edges.append((w, b, a)) 

edges.sort()



answer = 0
# 간선을 하나씩 확인
for weight, start, end in edges:
    # 루트가 같음 = 사이클 = 잇지 않는다.
    if find(start) != find(end):
        union(start, end)
        answer += weight

print(answer)


'''
크루스칼 VS 프림
프림은 정점 위주의 알고리즘, 크루스칼은 간선 위주의 알고리즘
프림은 시작점을 정하고, 시작점에서 가까운 정점을 선택하면서 트리르 구성 하므로 그 과정에서 사이클을 이루지 않지만 크루스칼은 시작점을 따로 정하지 않고 최소 비용의 간선을 차례로 대입 하면서 트리를 구성하기 때문에 사이클이 이루어지는 항상 확인 해야한다.
프림의 경우 최소 거리의 정점을 찾는 부분에서 자료구조의 성능에 영향을 받는다.
크루스칼은 간선을 기준으로 정렬하는 과정이 오래 걸린다.
간선의 개수가 작은 경우에는 크루스칼, 간선의 개수가 많은 경우에는 프림.
'''
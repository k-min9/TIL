'''
LCA(Lowest Common Ancestor) : 최소 공통 조상
참고 강의 by 동빈나 : youtu.be/O895NbxirM8
1. 모든 노드에 대한 깊이와 2**i번째 부모(한단계 위 ~ 루트까지의 부모)를 계산하고 기록(dp) (루트 노드부터 dfs)
2. 최소 공통 조상을 찾을 두 노드를 확인
- 두 노드의 깊이가 동일하도록 거슬러 올라가기
- 이후에 부모가 같아질때까지 거슬러 올라가기


>> 노드마다 2**i번째 부모에 대한 정보까지 저장할 수 있는 parent 리스트를 만든다.
공간복잡도가 증가하지만 시간복잡도를 감소하는 tradeoff가 발생
15칸 올라가야되면 8칸 4칸 2칸 1칸씩 올라갈 수 있다. O(NM)의 시간복잡도가 O(MlogN)으로!

>> 11438에서 공부완료.
공간복잡도는 이게 조금 더 낫겠지만 굳이 열화시켜서 풀 필요 있나...?
'''
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


# 최대 깊이 log100000을 상수로 사용
LENGTH = 21


# 노드의 depth 기록
def dfs(x, depth):
    visited[x] = True
    depths[x] = depth

    for node in graph[x]:
        if visited[node]:
            continue

        # 우선 바로 위에 있는 부모 정보만 갱신
        parent[node][0] = x
        dfs(node, depth + 1)


# 모든 노드의 전체 부모 관계 갱신하기
def set_parent():
    dfs(1, 0)
    for i in range(1, LENGTH):
        for j in range(1, N + 1):
            # 각 노드에 대해 2**i번째 부모 정보 갱신
            parent[j][i] = parent[parent[j][i - 1]][i - 1]


def lca(a, b):
    # 무조건 b의 깊이가 더 깊도록 스왑
    if depths[a] > depths[b]:
        a, b = b, a

    # a와 b의 깊이 동일
    for i in range(LENGTH - 1, -1, -1):
        if depths[b] - depths[a] >= 2**i:
            b = parent[b][i]

    if a == b:
        return a

    # 올라가면서 공통 조상 찾기
    for i in range(LENGTH - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

N = int(input())
parent = [[0] * LENGTH for _ in range(N + 1)]
visited = [False] * (N + 1)
depths = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

m = int(input())

for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

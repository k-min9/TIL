'''
감상 : 저어는 아직도 노드를 정점이라고 부르는게 익숙하지 않아요
접근 : 
루트가 U인 서브 트리 노드 수 구하는 문제, 이지만 일단 숫자를 보니 DP 쓰는건 확정
전부 탐방할때 올바른 트리임이 보장 되니까 DFS 써도 되고, BFS 써도 되고...
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node):
    nodes[node] = 1
    visited[node] = 1
    # 돌아가면서 깊게 방문
    for i in trees[node]:
        if not visited[i]:
            dfs(i)
            nodes[node] = nodes[node] + nodes[i]
    return

# 정점 수, 루트 번호, 쿼리 수
N, R, Q = map(int, input().split())
trees = [[] for _ in range(N+1)]
nodes = [0] * (N+1)  # dp할 answer
visited = [0] * (N+1)

# 간선 수 : N - 1
for _ in range(N-1):
    nodeA, nodeB = map(int, input().split())
    trees[nodeA].append(nodeB)  # 무방향
    trees[nodeB].append(nodeA)  # 무방향

# 판 다 깔았고
dfs(R)
# print(nodes)

# 출력
for _ in range(Q):
    print(nodes[int(input())])


'''
뭐가 올바른 트리 보장이냐 하 씨;; 
sys.setrecursionlimit(100000) 이거 없어서 안돌아간거
뭘 잘 못쓴건 줄 알고 트리랑 오타만 30분간 찾음. BFS나 쓸 걸...
근데 저 문장 왜 최대치만 설정해놓는건데 메모리 먹음??
'''
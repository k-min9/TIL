# https://leetcode.com/problems/minimum-height-trees
# 풀이 : 리프노드제거 횟수 = 높이, 이때의 노드 = 루트

import collections

def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
    if n <= 1:
        return[0]
    
    # 그래프 구성(양방향)
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
        
    # 현 리프노드 전부 추가
    leaves = []
    for i in range(n+1):
        if len(graph[i]) == 1:
            leaves.append(i)
            
            
    # 반복 시작 (루트 노드는 2개까지다)
    while n>2:
        n-= len(leaves)
        new_leaves = []
        for leaf in leaves:
            # print(graph)
            # print(leaves)
            # print(new_leaves)
            next_node = graph[leaf].pop()
            graph[next_node].remove(leaf)
            
            # 부모밖에 안남음 = 리프노드 됨
            if len(graph[next_node]) == 1:
                new_leaves.append(next_node)
                
        leaves = new_leaves
        
    return leaves
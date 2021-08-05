# https://leetcode.com/problems/course-schedule
# 풀이 2: DFS + 가지치기 

import collections

def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()
    visited = set()
    
    def dfs(i):
        #  순환 구조면 False
        if i in traced:
            return False
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):  # 순환구조로 False 리턴시 밑도 False 리턴하는 구조
                return False
        
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)
        
        return True
    
    # 순환 구조 판별 본문
    for x in list(graph):
        if not dfs(x):
            return False
        
    return True
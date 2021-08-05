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

'''
<for x in list(graph):> 이 부분 list 안 붙이면 딕셔너리 순회 중 변경 오류가 발생 
이유는 없는 dic을 찾을 경우, defaultdict가 기본값을 생성하여 변경이 발생하기 때문
그래서 graph 앞에 list를 붙임
'''
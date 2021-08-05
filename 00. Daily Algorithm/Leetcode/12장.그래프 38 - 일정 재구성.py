# https://leetcode.com/problems/reconstruct-itinerary/
# 풀이 2: DFS 일정 + 딕셔너리 그래프의 역순 버전

import collections

def findItinerary(self, tickets: list[list[str]]) -> list[str]:
    graph = collections.defaultdict(list)
    # 뒤집힌 그래프 구성
    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)
        
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
    
    dfs('JFK')
    return route[::-1]

# 풀이 X : DFS 일정 + 애초에 deque를 쓰면 되잖아 인간들아 버전
def findItinerary(self, tickets: list[list[str]]) -> list[str]:
    graph = collections.defaultdict(collections.deque)
    # 뒤집힌 그래프 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
        
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].popleft())
        route.append(a)
    
    dfs('JFK')
    return route[::-1]
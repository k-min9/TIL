'''
감상 : 어제 한 위상정렬(장난감 조립) 역순으로 하면 금방 아닐까
키워드 : 그래프이론, 트리, DFS, BFS
접근 : 일단 시키는대로 합시다. 오늘의 기분은 BFS
'''
import sys
from collections import deque

n = int(input())

#BFS용 초기화
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

#트리(그래프) 간선 입력
for _ in range(n-1):
    nodeA, nodeB = map(int, sys.stdin.readline().split())
    graph[nodeA].append(nodeB) #방향성 없음
    graph[nodeB].append(nodeA) #방향성 없음

#부모 노드 담을 리스트 << 잘쓰면 visited 안 써도 되지 않나
answer = [0] * (n+1) 

def bfs(graph, start, visited):
    queue = deque([start]) #라이브러리 만세
    visited[start] = True #방문처리
    while queue: #큐 빌때까지 돌아라
        v = queue.popleft() #하나 뽑고
        for i in graph[v]: #뽑은 노드가 인접한 트리 확인
            # 큐 추가부분
            if not visited[i]:
                answer[i] = v # 내가 니 아빠임                
                queue.append(i)
                visited[i] = True

#실행
bfs(graph, 1, visited)

#정답
for i in range(2, n+1):
    print(answer[i])

'''
감상:
q = deque([start])와
q = deque()
q.append[start]은 같다

끝나고 늦었지만 역시 visited 안써도 됬던거 같다.
개선사항이 몇 가지 있긴 한데, 다음 BFS 문제때 하자.
'''
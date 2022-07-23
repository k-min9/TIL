'''
요즘 뭔가 제한 이라는 단어 보면 이분탐색부터 생각이 나버림...
시야를 좁게 가지지 말자...
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(mid):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now == end: 
            return True
        for next, weight in graphs[now]:
            if not visited[next] and mid <= weight:
                q.append(next)
                visited[next] = 1
    return False

N, M = map(int, input().split())
graphs = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graphs[a].append([b, c])
    graphs[b].append([a, c])

start, end = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
    visited = [0]*(N+1)
    mid = (low + high) // 2
    if bfs(mid): 
        low = mid + 1
    else: 
        high = mid - 1

print(high)

'''
그건 그렇고 그게 맞는듯. 
모의트럭이 통과할때까지 보내는건 브릿지 컨스트럭터가 생각난다...
'''
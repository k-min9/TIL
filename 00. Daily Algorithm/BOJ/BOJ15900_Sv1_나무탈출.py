'''
[리프노드-루트노드까지의 거리]의 총 합이 홀수냐 짝수냐를 묻는 문제...인가?
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graphs = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

q = deque()
# 노드번호, 거리
q.append([1,0])
visited = [0] * (N+1)
visited[1] = 1

answer = 0
while q:
    cur, dist = q.popleft()
    # 리프 여부 체크
    flag = True
    for next in graphs[cur]:
        if not visited[next]:
            q.append([next, dist+1])
            visited[next] = 1
            flag = False
    if flag:
        answer += dist

if answer%2:
    print('Yes')
else:
    print('No')


'''
한 붓 그리기가 가능한지 묻는 문제
1. 한덩어리인가 2. 홀수인 경로가 2개거나 없는가
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**5)

def dfs(node):
    for next in graphs[node]:
        if not visited[next-1]:
            visited[next-1] = 1
            dfs(next)

v, e = map(int, input().split())
adj = [0]*v
visited = [0]*v
graphs = defaultdict(list)

for i in range(e):
    a, b = map(int, input().split())
    adj[a-1] += 1
    adj[b-1] += 1
    graphs[a].append(b)
    graphs[b].append(a)

odd = 0
for i in range(v):
    if adj[i] % 2 == 1:
        odd += 1

if odd == 1 or odd > 2:
    print('NO')

else:
    visited[0] = True
    dfs(1)
    for elem in visited:
        if not elem:
            print('NO')
            quit()
    print('YES')

'''
분리 집합부터 떠올렸는데 애초에 거기까지 갈 필요가 없었다
공부부족!
'''
import sys
input = sys.stdin.readline


def dfs(start):
    global cnt
    visited[start] = 1
    for i in graphs[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1

N = int(input())
M = int(input())
graphs = [[]*N for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graphs[a].append(b)
    graphs[b].append(a)
    
cnt = 0
visited = [0]*(N+1)

dfs(1)
print(cnt)

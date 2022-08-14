'''
트리 + DP
dp[i][0] : i 노드 포함하였을때 총합 최대값
dp[i][1] : i 노드 포함안하였을때 총합 최대값
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(cur):
    visited[cur] = 1
    for next in graphs[cur]:
        if not visited[next]:
            dfs(next)
            dp[cur][1] += dp[next][0]  # next를 선정
            dp[cur][0] += max(dp[next][0], dp[next][1])  # next 미선정

N = int(input())
nums = [0] + list(map(int, input().split()))
visited = [0]*(N+1)
dp = [[0, nums[i]]*2 for i in range(N+1)]

graphs = [list() for _ in range(N+1)]
for i in range(N-1):
    v, u = map(int, input().split())
    graphs[v].append(u)
    graphs[u].append(v)

dfs(1)
print(max(dp[1][0], dp[1][1]))

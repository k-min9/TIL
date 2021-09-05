'''
루트로부터 거리 짝수노드 수랑 홀수 노드 수 비교 아닐까?!
1차풀이 >> 아니었당! 애초에 예제 2 그려만 봤어도 아닌거 알 수 있었다.
그 노드가 얼리어댑터일때 그 노드를 루트로 가지는 서브 트리의 최소 필요 얼리어댑터를 더하면서 올라간다.
는 건 알겠는데!~~!!!!!
'''
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start):
#     q = deque()
#     q.append(start)
#     visited[start] = 1

#     answer = 0
#     while q:
#         cur = q.popleft()
#         for next in graphs[cur]:
#             if not visited[next]:
#                 q.append(next)
#                 visited[next] = visited[cur] + 1
#                 if visited[next] % 2 == 0:
#                     answer += 1

#     return min(answer, N-answer)

# N = int(input())
# graphs = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a, b = map(int, input().split())
#     graphs[a].append(b)
#     graphs[b].append(a)

# visited = [0]*(N+1)

# print(bfs(1))

'''
2차 풀이
dp[현재 노드][얼리 어답터 여부] = 현재 노드를 루트로 하는 서브트리가 필요로 하는 최소 얼리어답터 수
내가 얼리어답터면 자식이 얼리어답터인지 아닌지 상관없어지니까 가장 작은거 하나 더하면 됨
내가 얼리어답터가 아니면 자식이 전부 얼리어답터일때의 dp를 죄다 더하면 됨
'''
import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

def dfs(i):
  visited[i] = 1
  dp[i][0] = 0
  dp[i][1] = 1

  for next in graphs[i]:
    if not visited[next]:
      dfs(next)
      dp[i][0] += dp[next][1]
      dp[i][1] += min(dp[next][0], dp[next][1])

N = int(input())

graphs = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

dp = [[0]*2 for _ in range(N+1)]
visited = [0]*(N+1)
dfs(1)

print(min(dp[1][0], dp[1][1]))
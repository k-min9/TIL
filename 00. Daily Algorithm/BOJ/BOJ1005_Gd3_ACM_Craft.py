'''
전형적 위상정렬
'''
import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    # 건물의 갯수, 건설 순서 규칙
    N, K = map(int,input().split())
    # 건설 건축 시간
    times = list(map(int,input().split()))
    graphs = [[] for _ in range(N+1)]
    indegree = [0]*(N+1)
    dp = [0]*(N+1)

    for _ in range(K):
        X, Y = map(int,input().split())
        graphs[X].append(Y)
        indegree[Y] += 1

    que = deque()
    for i in range(1,N+1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = times[i-1]

    while que:
        cur = que.popleft()
        for next in graphs[cur]:
            dp[next] = max(dp[next], dp[cur] + times[next-1])
            indegree[next] -= 1
            if indegree[next] == 0:
                que.append(next)

    print(dp[int(input())])
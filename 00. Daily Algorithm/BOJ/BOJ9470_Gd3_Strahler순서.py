'''
위상정렬 최대 레벨 묻는 문제 같은데
'''
import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    # 테스트 번호, 노드 수, 간선 수
    K, M, P = map(int,input().split())
    graphs = [[] for _ in range(M+1)]
    indegree = [0]*(M+1)
    dp = [0]*(M+1)  # strahler 순서
    dp2 = [0]*(M+1)  # 강에 흘러들어오는 양

    for _ in range(P):
        X, Y = map(int,input().split())
        graphs[X].append(Y)
        indegree[Y] += 1

    que = deque()
    for i in range(1, M+1):
        if indegree[i] == 0:
            que.append(i)
            dp[i] = 1

    while que:
        cur = que.popleft()
        for next in graphs[cur]:
            indegree[next] -= 1
            if dp[next] < dp[cur]:
                dp[next] = dp[cur]
                dp2[next] = 1
            elif dp[next] == dp[cur]:
                dp2[next] += 1
            
           
            if indegree[next] == 0:
                # 0일때는 이미 순서 계산 종료 났으니
                if dp2[next] > 1:
                    dp[next] += 1
                que.append(next)

    print(K, dp[M])

'''
문제 자체가 이해가 잘 안되서 고생함 @.@
'''
'''
주의 포인트 
마이너스 간선 거리 = 벨만 - 포드를 써라 (다익스트라는 사이클 순환시 망함)
벨만 포드 : 사이클 마이너스 무한스파이럴 시 탈출, O(N^2)
'''

import sys
input = sys.stdin.readline

INF = sys.maxsize

def bellmanFord():
    global isPossible
    
    for repeat in range(N):
        for i in range(1, N + 1):
            for next, dist in graph[i]:
                if dp[i] != INF and dp[next] > dp[i] + dist:
                    dp[next] = dp[i] + dist
                    # 음의 싸이클 체크 = N-1바퀴 돌아도 갱신중
                    if repeat == N - 1:
                        isPossible = False


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
dp = [INF] * (N + 1)
dp[1] = 0

#음의 싸이클 체크
isPossible = True

for _ in range(M):
    a, b, c = map(int ,input().split())
    graph[a].append([b, c])

bellmanFord()

if not isPossible:
    print(-1)
else:
    # 오우야
    for i in dp[2:]:
        print(i if i != INF else -1)
'''
마이너스 간선 => 다익스트라는 봉인,  벨만 - 포드를 써라
이번 문제 질문 : 음의 사이클이 존재하는가?
'''
import sys
input = sys.stdin.readline

# 상수
INF = 1e9

def bellmanFord():
    global isPossible
    
    for repeat in range(N):
        for i in range(1, N + 1):
            for next, dist in graphs[i]:
                if dp[next] > dp[i] + dist:
                    dp[next] = dp[i] + dist
                    # 음의 싸이클 체크 = N-1바퀴 돌아도 갱신중
                    if repeat == N - 1:
                        isPossible = False
    
    print(dp)

for _ in range(int(input())):
    # 지점 수, 도로 수, 웜홀 수
    N, M, W = map(int, input().split())

    graphs = [[] for _ in range(N + 1)]
    dp = [INF] * (N + 1)
    dp[1] = 0


    # 도로, 플러스 간선, 무방향
    for _ in range(M):
        start, end, time = map(int, input().split())
        graphs[start].append((end, time))
        graphs[end].append((start, time))

    # 웜홀, 마이너스 간선, 방향
    for _ in range(W):
        start, end, time = map(int, input().split())
        graphs[start].append((end, -time))
        

    # 벨만 포드 시작
    isPossible = True

    bellmanFord()

    if isPossible:
        print("NO")
    else:
        print("YES")
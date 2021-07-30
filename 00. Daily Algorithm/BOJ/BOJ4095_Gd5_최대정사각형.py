'''
2차원 DP. 항상 방심하지 말고 손으로 직접 그려보면서 해보자
'''

while(True):
    N, M = map(int, input().split())
    # 종료 조건
    if N == 0 and M == 0:
        break

    # 매번 할 때마다 힘든 입력 시간
    graph = [[0]*(M+1) for _ in range(N+1)] # 2차원 DP
    
    for i in range(N):
        graph[i+1] = [0] + list(map(int, input().split()))
    
    # 보는 곳 (위 왼쪽 대각선) 중 가장 작은값 + 1 (0도 자동 처리)
    max_len = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if graph[i][j]:  # 본인이 0이 아님
                graph[i][j] = min(graph[i-1][j], graph[i][j-1], graph[i-1][j-1]) + 1
                max_len = max(max_len, graph[i][j])

    # 출력
    print(max_len)
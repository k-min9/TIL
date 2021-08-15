import sys
input = sys.stdin.readline

INF = 1e9
N, M = map(int, input().split())

# 인풋
maps = [[INF]*(N+1) for _ in range(N+1)]

# 알기 쉽게 말해서, 이미 길이 지어져있으면 노 코스트, 지어야지 갈 수 있을 경우 코스트 1
for _ in range(M):
    start, end, b = map(int, input().split())
    maps[start][end] = 0
    maps[end][start] = 1-b  # 코스트
for i in range(1, N+1):
    maps[i][i] = 0

# for m in maps:
#     print(*m)   

# 플로이드
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]

# for m in maps:
#     print(*m)

# 출력(질문 수)
K = int(input())
for _ in range(K):
    start, end = map(int, input().split())
    print(maps[start][end])
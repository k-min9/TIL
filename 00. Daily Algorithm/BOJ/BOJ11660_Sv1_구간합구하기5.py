'''
이걸 어디까지 가려나
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(N):
    maps[i+1] = [0] + list(map(int, input().split()))

# 누적 합
for i in range(1, N + 1):
    for j in range(1, N + 1):
        maps[i][j] = maps[i - 1][j] + maps[i][j - 1] + maps[i][j] - maps[i - 1][j - 1]

# for m in maps:
#     print(*m)

# 탐방 시작
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(maps[x2][y2] - maps[x1-1][y2] - maps[x2][y1-1] + maps[x1-1][y1-1])
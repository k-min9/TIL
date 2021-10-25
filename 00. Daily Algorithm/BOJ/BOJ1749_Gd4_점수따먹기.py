'''
누ㅡ적합
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
maps = [[0]*(M+1)]
for _ in range(N):
    maps.append([0]+list(map(int, input().split())))

# 누적 합
for y in range(1, N+1):
    for x in range(1, M+1):
        maps[y][x] = maps[y-1][x] + maps[y][x-1] + maps[y][x] - maps[y-1][x-1]
 
# for m in maps:
#     print(*m)

# 출력(O(N^4))
answer = -987654321
for y1 in range(1, N+1):
    for x1 in range(1, M+1):
        for y2 in range(y1, N+1):
            for x2 in range(x1, M+1):
                answer = max(answer, maps[y2][x2] - maps[y2][x1-1] - maps[y1-1][x2] + maps[y1-1][x1-1])

print(answer)
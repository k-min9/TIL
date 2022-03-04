'''
플로이드 와샬 후 모든 경로에 대한 이동비용 계산 후 최대값의 최소가 되는 경우 출력
'''
import sys
input = sys.stdin.readline


# 상수
INF = float('inf')

# 도시의 개수, 도로의 개수, 시간
N, M = map(int,input().split())
graph = [[0 if x == y else INF for y in range(N+1)] for x in range(N+1)]

# 시간
for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = min(graph[x][y],pay)
# 총 인원, 도시 번호
K = int(input())
friend_list = list(map(int,input().split()))

for mid in range(1,N+1):
    for end in range(1,N+1):
        for start in range(1,N+1):
            if graph[start][end] > graph[start][mid] + graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

min_value = INF
min_list = []
for city in range(1,N+1):
    temp_max = 0
    for p_num in friend_list:
        if graph[p_num][city] + graph[city][p_num] > temp_max:
            temp_max = graph[p_num][city] + graph[city][p_num]

    if temp_max < min_value:
        min_value = temp_max
        min_list = [city]
    elif temp_max == min_value:
        min_list.append(city)

print(*min_list)



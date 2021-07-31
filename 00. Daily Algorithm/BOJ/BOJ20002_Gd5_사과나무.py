'''
어제 최대사각형보다 쉬운 2차원 DP 
...아마
'''

import sys
input = sys.stdin.readline

# 과수원 크기
N = int(input())

# 입력 시간
graph = [[0]*(N+1) for _ in range(N+1)]  # 2차원 DP

for i in range(N):
    graph[i+1] = [0] + list(map(int, input().split()))

# 누적합 그래프에 작성
for i in range(1,N+1):
    for j in range(1,N+1):
            graph[i][j] = graph[i-1][j] + graph[i][j-1] + graph[i][j] - graph[i-1][j-1]

#print(graph)

# 각 위치에서 최대 값 
# (N^3 = 2700만 인것처럼 보이지만 K 크기가 감소하는 만큼 돌릴 수 있다! ... 아마)
answer = graph[1][1] # 최대값만 필요하니 DP 하지는 않는다.
for k in range(N):
    for i in range(1,N-k+1):
        for j in range(1,N-k+1):
                answer = max(answer, graph[i+k][j+k] - graph[i-1][j+k] - graph[i+k][j-1] + graph[i-1][j-1])

print(answer)

'''
pypy 아니면 시간 초과!!! 
pypy는 224ms에 모든것을 해결해줍니다.
'''
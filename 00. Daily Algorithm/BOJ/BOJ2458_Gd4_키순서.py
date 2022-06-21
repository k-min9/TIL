'''
옛날 푼 문제중에 역사였나 하는 문제가 있었음
그거랑 같은 플로이드-와셜 문제
'''
import sys

#입력
N, M = map(int, input().split())
height = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall, short = map(int, sys.stdin.readline().split())
    height[tall][short] = 1

#플로이드 와샬 알고리즘
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 작은 경우
            if height[i][j] == 1 or (height[i][k] ==1 and height[k][j] == 1):
                height[i][j] = 1

#출력
answer = 0
for i in range(1, N+1):
    known_height = 0
    # 자신보다 작은 사람과 큰사람 합을 구해서 N-1이면 자기 위치를 아는거임
    for j in range(1, N+1):
        known_height += height[i][j] + height[j][i]
    if known_height == N-1:
        answer += 1
print(answer)

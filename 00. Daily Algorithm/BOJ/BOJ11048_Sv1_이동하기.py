'''
감상 : 전형적인 2차원 DP
단지 어차피 DP 전 범위 다 할거고, 대각선 이동은 모든 경우에서 손해다. 계산 안해도 됨. 
'''

#전처리
import sys
input = sys.stdin.readline

#그래프
N, M = map(int, input().split())
answer = [[0]*(M+1) for _ in range(N+1)] 
# 와꾸가 필요 없다고 생각했는데, 
# 필요했다. 정답은 (M+1)*(N+1)와꾸로 담아야 초기치를 입력한것이 됨 아니면 그래프를 복잡하게 받던가

#초기 사탕 배치
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

#DP의 기본은 bottom up
for i in range(N):
    for j in range(M):
        answer[i+1][j+1] = graph[i][j] + max(answer[i+1][j], answer[i][j+1]) #대각선 이동 무시


print(answer[N][M])

'''
배운것 : 
위에서 전형적인 2차원 DP라고 말했지만 푸는데 오래걸림
이번 실책은 시작할때 N*M 사이즈의 그래프를 만든것이다.
list관련 index 에러 바로 났고, 초기값 지정이 없이 없는 곳을 골랐다는걸 깨달음

평소처럼 N*M의 그래프외에도 (N+1)*(M+1)사이즈의 answer 그래프를 썼다.
메모리 차이 얼마 안날거 같은데 가독성 차이는 엄청 클듯.
'''

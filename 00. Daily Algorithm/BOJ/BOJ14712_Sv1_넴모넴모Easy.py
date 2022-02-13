'''
프로젝트 마지막 주, 시간 없고 바쁠때는 점심먹으면서 다른 사람 코드 보고 학습합니당!
그래도 코딩은 라이브 코딩함!
백트래킹 문제인거 파악완료!
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graphs = [[0]*(M+1) for _ in range(N+1)]
answer = 0

def dfs(cnt):
    global answer
    if cnt == N * M:
        answer += 1
        return
    
    # 평소에 쓰는 MOVES의 수식 버전 (0,0), (0,1), (1,0), (1,1) => (y,x) = (cnt//x, cnt%X)
    y = cnt // M + 1
    x = cnt  % M + 1
    
    # 그냥 네모를 놓치 않거나
    dfs(cnt + 1)

    # 네모를 놓을 수 있으니 놓는 경우
    if graphs[y - 1][x] == 0 or graphs[y][x - 1] == 0 or graphs[y - 1][x - 1] == 0: 
        graphs[y][x] = 1
        dfs(cnt + 1)
        graphs[y][x] = 0
        
        
dfs(0)
print(answer)

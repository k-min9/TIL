'''
백트래킹하면서 무지성으로 풀면 될것 같다.
'''
import sys
input = sys.stdin.readline


# 상수
MOVES = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def backtrack(x, y, cnt, sums):
    # 종료
    if cnt == K:
        global answer
        answer = max(answer, sums)
        return
    
    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            # 본인 체크
            if visited[i][j]:
                continue
            # 인접 체크
            for dx, dy in MOVES:
                nx = i + dx
                ny = j + dy
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]:
                    break
            else:
                visited[i][j] = 1
                backtrack(i, j, cnt+1, sums+graphs[i][j])
                visited[i][j] = 0


# 크기, 선택 수
N, M, K = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]

answer = -987654321
visited = [[0]*M for _ in range(N)]
backtrack(0, 0, 0, 0)
print(answer)

'''
백트래킹에 return을 안붙인 멍청이가 있었다고 합니다.
ㄴ그게 접니다.
와ㅡ우
for j in range(y if i == x else 0, M):
'''
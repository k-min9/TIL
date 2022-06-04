'''
n = 12 > n-queen과 비슷한 냄새가 난다.
백트래킹 구현일듯
'''
import sys
input = sys.stdin.readline


def backtrack(x):
    global answer
    if x == 2*N + 1:
        answer += 1
        return
    if arr[x] != 0:
        backtrack(x+1)
    else:
        for i in range(1, N+1):
            if not visited[i] and x+i+1 < 2*N+1 and arr[x+i+1] == 0:
                visited[i] = 1
                arr[x] = i
                arr[x+i+1] = i
                backtrack(x+1)
                visited[i] = 0
                arr[x] = 0
                arr[x+i+1] = 0


# 길이, X=Y
N, X, Y = map(int, input().split())
visited = [0]*(N+1)
arr = [0]*(2*N+1)
# 길이 차이가 그 수치니까 오히려 좋아
visited[Y-X-1] = 1
arr[X] = Y-X-1 
arr[Y] = Y-X-1

# 계산
answer = 0
backtrack(1)
print(answer)

'''
내가 잘못짠걸수도 있긴한데 생각이상으로 백트래킹이 아니어따
'''
'''
N이 8이하 = 완전탐색해라
애초에 이거 완전 탐색 말고 다른 방법을 모르겠음
'''
import sys
input = sys.stdin.readline


def dfs(sums, cnt):
    if cnt == N:
        global answer
        answer += 1
        return
    
    for i in range(N):
        if not visited[i]:
            sums_next = sums + kits[i] - K
            if sums_next >= 0:
                visited[i] = 1
                dfs(sums_next, cnt+1)
                visited[i] = 0


# 운동키트 수, 체감
N, K = map(int, input().split())
kits = list(map(int, input().split()))
visited = [0]*N
answer = 0
sums = 0

dfs(0, 0)
print(answer)


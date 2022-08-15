'''
문제가 유사하길래 복습
'''
import sys
input = sys.stdin.readline

def dfs(depth, idx, N, M):
    if depth == M:
        print(*answer)
        return

    for i in range(idx, N):
        answer.append(nums[i])
        dfs(depth+1, i, N, M)
        answer.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
answer = []

dfs(0, 0, N, M)
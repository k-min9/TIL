'''
기초 공부빠르게!
'''
import sys
input = sys.stdin.readline

def dfs(depth, N, M):
    if depth == M:
        print(*answer)
        return

    for i in range(N):
        answer.append(nums[i])
        dfs(depth+1, N, M)
        answer.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
answer = []

dfs(0, N, M)

'''
2분!
'''
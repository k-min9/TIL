'''
정렬해서 투 포인터로 삭삭삭 풀면 됨. 
도중에 M과 같을때 탈출하면 더 빠르겠지만 스킵
'''
import sys
input = sys.stdin.readline

# 수열 길이, 조건 : M이상 차이를 내시오
N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]

nums.sort()
l, r = 0, 0
answer = sys.maxsize

while l<N and r<N:
    if nums[r] - nums[l] < M:
        r += 1
    else:
        answer = min(answer, nums[r] - nums[l])
        l += 1

print(answer)
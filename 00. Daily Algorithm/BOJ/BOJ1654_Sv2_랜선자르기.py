'''
보는 순간 이분탐색
인기 많네 이런 타입;;;
'''
import sys
input = sys.stdin.readline

# N개 만들기
K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]

start, end = 1, max(nums)
while start <= end:
    mid = (start + end) // 2

    lines = 0 
    for i in nums:
        lines += i // mid 
        
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)

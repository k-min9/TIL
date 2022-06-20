'''
숫자가 겁나 큼 = 스스로 이진탐색으로 풀라고 알려주는거나 다름없음
'''
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
levels = [ int(input()) for _ in range(N)]

start = min(levels)
end = start + K

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    sums = 0
    for level in levels:
        if mid > level:
           sums += (mid - level)
           
    if sums <= K:
        start = mid+1
        answer = max(mid, answer)
    else:
        end = mid -1


print(answer)

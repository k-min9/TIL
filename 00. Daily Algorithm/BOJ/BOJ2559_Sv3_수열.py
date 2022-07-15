'''
누적합을 슬라이딩 윈도우하면 끝
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))
psum = [0] * (N+1)
s = 0
for i in range(N):
    s += nums[i]
    psum[i+1] = s
    
answer = -int(1e9)
for i in range(K, N+1):
    answer = max(answer, psum[i]-psum[i-K])
print(answer)

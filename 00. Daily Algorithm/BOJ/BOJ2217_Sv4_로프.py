'''
N번째 큰 수는 * N 을 곱할 수 있으니까...?
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)

# 계산
answer = 0
for i in range(N):
    answer = max(answer, nums[i] * (i+1))

# 정답
print(answer)

'''
DP 조차 필요없는디.,,,
'''

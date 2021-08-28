'''
카데인인 줄 알았는데 슬라이딩 윈도우;;;
기상청 너에게는 실망했다
'''
import sys
input = sys.stdin.readline

# 날짜 수 , 윈도우 크기
N, K = map(int, input().split())
nums = list(map(int, input().split()))

cur_sum = sum(nums[:K])
answer = cur_sum

for i in range(N-K):
    cur_sum -= nums[i]
    cur_sum += nums[i+K]
    answer = max(answer, cur_sum)

print(answer)

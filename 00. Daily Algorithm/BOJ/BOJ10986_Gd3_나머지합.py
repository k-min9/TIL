'''
누적합 : 나머지가 같음 = MOD가 같음 = 그 구간을 뺀 값은 M으로 나뉨
나머지 같은 값이 N개다 -> NC2개의 구간이 있음
'''
import sys
input = sys.stdin.readline

# 구간 수, 나눌 수
N, M = map(int, input().split())

nums = list(map(int, input().split()))
sums = [0] * M  # 누적합 나머지 모음
sums[0] = 1
sum = 0

for num in nums:
    sum += num
    sums[sum%M] += 1

answer = 0
for i in sums:
    if i > 1:
        answer += i * (i-1) // 2
    
print(answer)

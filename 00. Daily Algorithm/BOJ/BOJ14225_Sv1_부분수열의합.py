'''
N이 20이면 2^20 = 백만 정도? 완전 탐색
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 비트마스킹으로 합쳐보자
nums2 = set()
for i in range(1<<N):
    sums = 0
    for j in range(N):
        if i & (1<<j) != 0:
            sums += nums[j]
    nums2.add(sums)

# 1부터 답 나올때까지 쭉 진행
answer = 1
while True:
    if answer not in nums2:
        print(answer)
        break
    else:
        answer += 1

'''
그냥 비트마스킹 연습함
'''

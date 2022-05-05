'''
본질은 누적합인거 같긴한데, 순서가 바뀌지 않는 부분수열이라 더욱
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# 우선 총합이 4의 배수여야 함
if sum(nums) % 4:
    print(0)
else:
    cnt = [0]*4
    cnt[0] = 1 
    pSum = 0
    division = sum(nums)//4
    for num in nums:
        pSum += num
        if pSum == 3*division :
            cnt[3] += cnt[2]
        if pSum == 2*division :
            cnt[2] += cnt[1]
        if pSum == 1*division :
            cnt[1] += cnt[0]
            
    print(cnt[3])
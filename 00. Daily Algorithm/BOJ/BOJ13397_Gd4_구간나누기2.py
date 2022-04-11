'''
이분 탐색, 파라메트릭 서치
'''
import sys
input = sys.stdin.readline


def isValid(x):
    global result
    low = nums[0]
    high = nums[0]
    d = 1

    for num in nums:
        if high < num:
            high = num
        
        if low > num:
            low = num

        if high - low > x:
            d += 1
            low = num
            high = num
    
    return M >= d


N, M = map(int, input().split())
nums = list(map(int, input().split()))

r = max(nums)
l = 0

result = r
while l <= r:

    # 해당 답안으로 M개로 나눠지는지
    mid = (l+r) // 2
    if isValid(mid):
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1

print(result)



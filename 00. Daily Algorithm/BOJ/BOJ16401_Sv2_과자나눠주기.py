'''
파라메트릭~ 애초에 비슷한거 있지 않았나?
'''
import sys
input = sys.stdin.readline

# 조카 수, 과자 수
M, N = map(int, input().split())
nums = list(map(int, input().split()))
s, e = 1, max(nums)

answer = 0
while s<=e:
    # 몇개의 막대가 나오나
    sums = 0
    mid = (s+e) // 2    
    for num in nums:
        sums += (num//mid)
    
    # 조건 만족은 한데 더 가능할거 같음
    if sums >= M:
        answer = mid
        s = mid + 1
    else:
        e = mid - 1

print(answer)

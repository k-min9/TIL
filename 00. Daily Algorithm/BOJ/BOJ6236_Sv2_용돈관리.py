'''
이분 탐색으로 맞추려고 필사적인 문젠데;;;?
'''
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
costs = [int(input()) for _ in range(N)] 


# 이분 탐색
lo = 1
hi = 100000
answer = -1
while lo <= hi:
    mid = (lo+hi) // 2
    # 초회 인출
    money = mid
    num = 1
    # 진핸
    for cost in costs:
        if money < cost:
            money = mid
            num += 1
        money -= cost
    
    if num > M or mid < max(costs):
        lo = mid+1
    else:
        hi = mid-1
        answer = mid

print(answer)
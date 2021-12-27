'''
... 술을 왜 버려?!
라는 이유로 이해하는데 시간이 조금 걸린 문제...
그거랑은 별개로 이분탐색 문제다.
'''
import sys
input = sys.stdin.readline

# 주전자 수, 사람 수
N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]

answer = -1
lo, hi = 1, 2 ** 31
while lo <= hi:
    mid = (lo + hi) // 2
    # 잔 수
    cnt = 0
    for num in nums:
        cnt += num // mid
    # 이분 탐색
    if cnt >= K:
        answer = mid
        lo = mid+1
    else:
        hi = mid-1

print(answer)
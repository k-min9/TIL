'''
말도안되게 큰수, 비가역적 -> 이분 탐색
'''
import sys
input = sys.stdin.readline


def my_bisect(n):
    cnt = 0
    while n:
        cnt += n // 5
        n //= 5
    return cnt


N = int(input())

lo = 0 
hi = 1000000000

while lo + 1 < hi:
    mid = (lo+hi) // 2
    if my_bisect(mid) >= N:
        hi = mid 
    else:
        lo = mid 

if my_bisect(hi) == N:
    print(hi)
else:
    print(-1)

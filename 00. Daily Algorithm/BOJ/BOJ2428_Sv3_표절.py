'''
스터디 동료 풀이 리뷰 + 빠르게 리팩토링
N : 10만 > O(NlogN)이 국룰
'''
import sys
input = sys.stdin.readline

N = int(input())
files = sorted(list(map(float, input().split())))
count = 0
for i in range(N):
    l = i
    r = N
    while l < r:
        m = (l+r)//2
        if files[i]>=(0.9)*files[m]:
            l = m + 1
        else:
            r = m
    count += r-i-1

print(count)

'''
천잰가? 거기에 꼭 이분탐색 안해도 order 하는 순간부터 범위 잡아서 풀 수 있음
'''
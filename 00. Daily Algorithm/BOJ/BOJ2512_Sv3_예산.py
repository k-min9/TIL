'''
예산이 맞을때까지 이분 탐색!
'''
import sys
input = sys.stdin.readline

N = int(input())
needs = list(map(int, input().split()))
Money = int(input())

low, high = 0, max(needs)
while low <= high:
    mid = (low + high) // 2
    num = 0
    for need in needs:
        if need >= mid: 
            num += mid
        else: 
            num += need
    if num <= Money: 
        low = mid + 1
    else: 
        high = mid - 1

print(high)

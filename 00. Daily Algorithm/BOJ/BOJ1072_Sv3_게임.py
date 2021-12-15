'''
현 시점에서 얼마가 변했는지를 확인해서 이분
'''
import sys
input = sys.stdin.readline
 
# 입력 및 변수 설정
X, Y = map(int, input().split())
Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = X
 
    while left <= right:
        mid = (left + right) // 2
        if (Y+mid)*100 // (X+mid) <= Z:
            left = mid+1
        else:
            answer = mid
            right = mid - 1
 
    print(answer)
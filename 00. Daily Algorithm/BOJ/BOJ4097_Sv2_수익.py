'''
올만에 카데인 알고리즘
'''
import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N:
        nums = [int(input()) for _ in range(N)]
        answer = -987654321
        sums = 0 
        for num in nums:
            sums += num
            answer = max(answer, sums)
            if sums<0:
                sums = 0
        print(answer)
    else:
        break
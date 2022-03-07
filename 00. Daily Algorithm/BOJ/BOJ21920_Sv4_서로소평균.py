'''
평범한 정수론 문제...
'''
import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
nums = list(map(int, input().split()))
X = int(input())

# 서로소 최소 숫자
num_cnt = 0
num_sum = 0
for num in nums:
    if gcd(num, X) == 1:
        num_cnt += 1
        num_sum += num

print(num_sum/num_cnt)

'''
뭐가 하고 싶었는데 실버4임...?
'''
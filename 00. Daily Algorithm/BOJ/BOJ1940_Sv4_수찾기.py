'''
이분탐색보다 해쉬가 빠를거 같은데...?
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = set(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

for query in queries:
    if query in nums:
        print('1')
    else:
        print('0')

'''
맞네
'''
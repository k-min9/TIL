'''
파이썬이라?
'''
import sys
input = sys.stdin.readline

nums = list(set(int(input()) for _ in range(int(input()))))
nums.sort()

for num in nums:
    print(num)

'''
...?!
'''
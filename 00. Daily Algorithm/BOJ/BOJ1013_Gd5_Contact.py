'''
문자열 강화기간
정규 표현식 (실제로 있는)
'''
import sys
input = sys.stdin.readline
import re

for _ in range(int(input())):
    nums = input().strip()
    pattern = re.compile('(100+1+|01)+')
    if pattern.fullmatch(nums):
        print("YES")
    else:
        print("NO")

'''
정규 표현식(+파이썬)에 관해서는 따로 정리해두겠음!
'''
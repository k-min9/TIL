'''
문자열 좋아 + 정규식 버전
+ : 앞 문자가 한번 이상 등장함
() : 하나로 묶음
| : 또는
'''
import sys
input = sys.stdin.readline
import re

words = input().rstrip()
pattern = re.fullmatch('(pi|ka|chu)+', words)

if pattern:
    print('YES')
else:
    print('NO')

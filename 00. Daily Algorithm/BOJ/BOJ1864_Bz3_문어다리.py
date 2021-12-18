'''
프로젝트 중간에 간단한 손 풀기
'''
import sys
input = sys.stdin.readline

d = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    s = input().rstrip()
    if s == '#':
        break
    res = 0
    for i in range(len(s)):
        res += d[s[i]] * 8**(len(s)-i-1)
    print(res)
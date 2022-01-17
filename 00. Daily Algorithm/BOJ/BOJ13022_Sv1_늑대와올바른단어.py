'''
문자열 체크하기 = 파이썬 본령 발휘
'''
import sys
input = sys.stdin.readline

checks = list()
for i in range(13, 0, -1):
    checks.append('w'*i + 'o'*i + 'l'*i + 'f'*i)

words = input().rstrip()

for check in checks:
    while check in words:
        words = words.replace(check, 'X')

if 'w' in words or 'o' in words or 'l' in words or 'f' in words:
    print(0)
else:
    print(1)
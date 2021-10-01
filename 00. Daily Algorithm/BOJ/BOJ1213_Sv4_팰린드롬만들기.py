'''
접근 : 홀수 1개까지 허용
최대 50글자... 카운터로 바꾸면 대문자 26글자
카운터 연습
'''
import sys
input = sys.stdin.readline
from collections import Counter

counter = sorted(Counter(input().rstrip()).items())

answer = ''
answer_odd = ''
odd_num = 0
for k, v in counter:
    if v % 2 == 1:
        odd_num += 1
        answer_odd = k
    answer += k * (v//2)

if odd_num <= 1:
    print (answer + answer_odd + answer[::-1])
else:
    print("I'm Sorry Hansoo")
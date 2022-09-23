'''
브론즈를 브론즈 답지 않게 푸는 법
표현 정규식
'''
import sys
import re
input = sys.stdin.readline

words = input().rstrip()
words_list = re.split('(?=[A-Z])', words)  # 대문자로 나누기

cnt = 0    
for i in range(1, len(words_list)-1):
    a= len(words_list[i]) % 4
    if a!= 0: 
        cnt+=(4-a)    
print(cnt)

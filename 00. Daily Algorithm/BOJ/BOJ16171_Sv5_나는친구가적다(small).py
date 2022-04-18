'''
문자열 제어
'''
import sys
input = sys.stdin.readline

words = input().rstrip()
words2 = ''
for word in words:
    if word in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        words2 += word

answer = 0
query = input().strip()
if query in words2:
    answer = 1

print(answer)

'''
0~9를 제거하는 쪽은 틀림
이상한데서 시간이 끌리네에...
'''
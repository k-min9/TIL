'''
라스트 워드 : E로 시작하는 괄호 문제
'''
import sys
input = sys.stdin.readline

N = int(input())
words = input().rstrip()

flag = True
word_last = 'E'
answer = 0
for word in words:
    if word_last != word:
        if flag:
            answer += 1
            flag = False
        else:
            flag = True
    word_last = word
if flag:
    answer += 1

print(answer)
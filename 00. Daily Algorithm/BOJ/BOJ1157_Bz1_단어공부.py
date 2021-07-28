'''
딕셔너리 함수 쓸데 없이 안 익숙해...
'''

import sys
input = sys.stdin.readline

words = input().strip()
words = words.upper()

answer = {}
for word in words:
    answer[word] = answer.get(word,0)+1

answer = sorted(answer.items(), key=lambda x : x[1])

if len(answer) == 1:
    print(answer[-1][0])
elif answer[-1][1] == answer[-2][1]:
    print('?')
else:
    print(answer[-1][0])
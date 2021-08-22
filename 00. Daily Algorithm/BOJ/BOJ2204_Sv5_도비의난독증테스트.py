'''
파이썬은 문자열 비교 진짜 쉬움
'''

import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    answer = ''
    answer_min = 'z'*1000    
    for _ in range(N):
        word = input().rstrip()
        word_lower = word.lower()
        if answer_min > word_lower:
            answer_min = word_lower
            answer = word
    print(answer)

'''
min에 인덱스 섞으면 이거보다 짧게할 수는 있음
'''
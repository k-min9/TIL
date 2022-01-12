'''
문자열 변환 = 파이썬 특기 
'''
import sys
input = sys.stdin.readline

words = input().rstrip()
keys = input().rstrip()
words_len = len(words)
keys_len = len(keys)

answer = ''
for idx in range(words_len):
    i = idx % keys_len
    if words[idx] == ' ':
        answer += ' '
    else:
        move = ord(keys[i]) - ord('a') + 1
        if ord('a') <= ord(words[idx])- move < ord('a') + 26:
            answer += chr(ord(words[idx])-move)
        else:
            answer += chr(ord(words[idx])-move + 26)
print(answer)
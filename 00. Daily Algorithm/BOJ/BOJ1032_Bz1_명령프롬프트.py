'''
첫 문자여 저장해두고 미스매칭할때마다 변경후 조립하여 출력
'''
import sys
input = sys.stdin.readline

N = int(input())
texts = list(input())
texts_len = len(texts)
for i in range(N - 1):
    b = list(input())
    for j in range(texts_len):
        if texts[j] != b[j]:
            texts[j] = '?'
print(''.join(texts))

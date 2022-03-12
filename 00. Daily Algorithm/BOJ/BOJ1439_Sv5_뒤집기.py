'''
스택...이었던가?
'''
import sys
input = sys.stdin.readline

cnt = 0
str = input().rstrip()
before = ''
for s in str:
    if s != before:
        cnt += 1
    before = s

print(cnt//2)

'''
스택 전에 일단 종이에 적은걸 식으로 옮겼는데 그대로 끝나버렸다;;
'''
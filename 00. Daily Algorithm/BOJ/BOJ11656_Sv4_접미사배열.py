'''
파이썬이라 날로 먹는 문제가 되버린거 같은데...
'''
import sys
input = sys.stdin.readline

words = input().rstrip()
words_list = list()

for i in range(len(words)):
    words_list.append(words[i:])

words_list.sort()

for answer in words_list:
    print(answer)
    
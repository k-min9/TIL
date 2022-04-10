'''
문자열 조작 = 쉬움
# 특수한 무한 입력
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

word_dic = defaultdict(str)
word_set = set()

words1 = 'aiyeou'
words2 = 'bkxznhdcwgpvjqtsrlmf'

# 입력
for i in range(6):
    j = (i + 3) % 6
    word_dic[words1[i]] = words1[j]
    word_dic[words1[i].upper()] = words1[j].upper()
    word_set.add(words1[i])
    word_set.add(words1[i].upper())

for i in range(20):
    j = (i + 10) % 20
    word_dic[words2[i]] = words2[j]
    word_dic[words2[i].upper()] = words2[j].upper()
    word_set.add(words2[i])
    word_set.add(words2[i].upper())

for strings in sys.stdin:
    if not strings:
        break
    answer = ''
    for s in strings:
        if s in word_set:
            answer += word_dic[s]
        else:
            answer += s
    print(answer, end='')

'''
ㄹㅇ루다가! 문제 푸는 시간보다 입력하는 방법이 더 문제네 ㅡㅡ
'''
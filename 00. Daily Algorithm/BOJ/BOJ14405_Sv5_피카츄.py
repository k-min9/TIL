'''
문자열 좋아
'''
import sys
input = sys.stdin.readline

words = input().rstrip()
words = words.replace('pi','#')
words = words.replace('ka','#')
words = words.replace('chu','#')
words = words.replace('#','')

if words:
    print('NO')
else:
    print('YES')

'''
반례 : pkai 때문에 # 넣음
'''
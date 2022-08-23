'''
초심?
class 문제 미는중
'''
import sys
input = sys.stdin.readline

words = list(set(input().strip() for _ in range(int(input()))))

# 단어 순 정렬 후, 길이 정렬하면 요건 만족
words.sort()
words.sort(key=len)

for word in words:
    print(word)

'''
생각보다 빡센데??
'''
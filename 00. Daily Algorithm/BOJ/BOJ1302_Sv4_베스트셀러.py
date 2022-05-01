'''
Counter = 사기
'''
from collections import Counter
import sys
input = sys.stdin.readline

books = [input().rstrip() for _ in range(int(input()))]
books.sort()

print(Counter(books).most_common(1)[0][0])
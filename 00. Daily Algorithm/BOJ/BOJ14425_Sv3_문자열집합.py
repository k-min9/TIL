'''
set과 list는 검색 속도가 다르다. 끝
'''


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = set()
for _ in range(n):
    words.add(input().strip())
    
cnt = 0
for _ in range(m):
    if input().strip() in words:
        cnt = cnt + 1
print(cnt)
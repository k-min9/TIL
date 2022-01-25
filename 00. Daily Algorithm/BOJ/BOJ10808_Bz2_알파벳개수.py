import sys
from collections import Counter
input = sys.stdin.readline


chars = list(map(str, input().strip()))
chars = Counter(chars) # 알파벳 개수를 확인
answers = list()

# 알파벳 개수만큼 반복
for i in range(26):
    answers.append(chars[chr(97 + i)])

print(*answers)

'''
defaultdict와 Counter 쓰면 끝!
'''
import sys
input = sys.stdin.readline
from collections import Counter, defaultdict

formats = defaultdict(int)
for _ in range(int(input())):
    a, format = input().strip().split(".")
    formats[format] += 1

formats_counter = Counter(formats)
formats_counter = sorted(formats_counter.items(), key=lambda x : x[0])

for format, num in formats_counter:
    print(format, num)

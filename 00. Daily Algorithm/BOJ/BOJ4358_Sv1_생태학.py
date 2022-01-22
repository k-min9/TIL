'''
카운...터?
'''
import sys
from collections import Counter
input = sys.stdin.readline

trees = list()
while True:
    tree = input().strip()
    if tree:
        trees.append(tree)
    else:
        break

N = len(trees)
counter = Counter(trees)
counter = sorted(counter.items())

for name, cnt in counter:
    print(name, f'{(100*cnt/N):.4f}')

'''
파이썬이 사기인건에 대하여
'''
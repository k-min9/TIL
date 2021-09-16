'''
이건 작은 순서부터 파송송하면 되는거 아닌가???
제목이 내 뇌를 침입해오고 있다;;;
'''

import sys
input = sys.stdin.readline

n = int(input())
sticks = sorted(list(map(int, input().split())))

answer = 0
total = sum(sticks)
for stick in sticks:
    total -= stick
    answer += stick * total
print(answer)
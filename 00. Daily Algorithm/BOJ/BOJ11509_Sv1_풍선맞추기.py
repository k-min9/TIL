'''
접근 : 딕셔너리다!!! 세트여도 되는데 마지막 높이 부분 계산하기 싫음
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
ballons = list(map(int, input().split()))
arrows = defaultdict(int)

for ballon in ballons: 
    if ballon in arrows:
        #print('pop!', end=' ')
        arrows[ballon] -= 1
        if arrows[ballon] == 0:
            del arrows[ballon]
        arrows[ballon-1] += 1
    else:
        #print('shoot!', end= '')
        arrows[ballon-1] += 1

    #print(arrows, sum(arrows.values()))

print(sum(arrows.values()))

'''
defaultdict 생기고 인생 너무 꿀잼 됨
솔직히 list 쓰면 되는 문제라고 생각하긴 하는데 얘는 N이 10억이어도 대응 가능함
'''
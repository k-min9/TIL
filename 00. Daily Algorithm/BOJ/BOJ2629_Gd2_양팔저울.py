'''
감상 : 
1. 추를 선택 
2. 무게를 더하거나 (안쓰거나) 빼거나
3. 각각의 결과를 추가
4. 추가 없어질때까지 반복
최악의 케이스(2^30)일 경우 매우 느림
'''

import sys
input = sys.stdin.readline #아직도 안 익숙한데...

#추(pendlum)
pendNum = int(input())
pends = list(map(int,input().split()))
#구슬(bead)
beadNum = int(input())
beads = list(map(int,input().split()))
#자동 중복 제거하는 집합 선택
grams = {0}

while pends:
    p = pends.pop() # 순서 상관없음
    new = set() #더하기용
    for gram in grams:
        new.add(gram+p)
        new.add(gram-p)
    grams = grams | new
    
for bead in beads:
    if bead in grams:
        print('Y', end=" ")
    else:
        print('N', end=" ")
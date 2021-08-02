'''
N은 10^5 요즘이런거 많네
이진 탐색 쓸 수 있는지 묻는 엑셀 같은 문제
'''

import sys
input=sys.stdin.readline

from bisect import bisect_left

# 칭호, 캐릭터 수
N,M = map(int,input().split())

# 칭호, 이름
names=[]
powers=[]

for _ in range(N):
    name, power = input().split()
    names.append(name)
    powers.append(int(power))

# 이진탐색 쓸 수 있는지 묻는 문제
for _ in range(M):
    chk = int(input())
    print(names[bisect_left(powers, chk)])
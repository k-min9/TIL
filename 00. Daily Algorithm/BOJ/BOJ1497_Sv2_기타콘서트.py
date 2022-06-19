'''
옛날 스터디원의 비트마스크 풀이 라이브 코딩
'''
import sys
input = sys.stdin.readline
from itertools import combinations

# 기타 플레이 리스트 이진수로 바꿔서 set에 저장.
N,M = map(int,input().split())
guitars = set()
for _ in range(N):
    name, pos = input().split()
    bin_change=''
    for chr in pos:
        if chr=="Y":
            bin_change += '1'
        else:
            bin_change += '0'
    guitars.add(int(bin_change,2))

# set에서 0 제거하고 비었으면 죄다 N이라는 소리니 -1출력 후 종료
guitars -={0}
if not guitars:
    print(-1)
    exit()

max_cnt=0
# 1개~N개까지 set에서 추출하는 조합 검사(N이 set길이 넘어가면 자동 종료.)
for i in range(1, N+1):
    for combs in combinations(guitars,i):
        # total에 각각 조합마다 이진수 연산.
        total=0
        for num in combs:
            total |=num
        # 연산한 total에서 Y몇 개인지 확인.
        cnt=0
        for j in range(M):
            if total&(1<<j):
                cnt+=1
        # max값 최신화 시켜주고 i를 오름차순 기록하여 최소 기타 파악
        if max_cnt < cnt:
            max_cnt = cnt
            max_guitar = i

print(max_guitar)

'''
??????????????????????
문제보다 내용에 정신이 멍해진다.
소가 최대 9마리면
1. itertools로 리스트 만들어서 전부 더한다음에 
2. isPrime 같은거 하나 만들어서 체크하고 넣으면 될 것 같다.
'''

# 기본 전처리
import sys
input = sys.stdin.readline
from itertools import combinations

# 1도 prime이라고 판정하는 멍청 판정
def is_Prime(num):
    for i in range(2,num):  # 1이랑 자기자신 빼고 나눠서 나눠지면 바로 break => 시간 확보
        if num%i==0:
            return False
    return True

N, M = map(int, input().split())
cows = list(map(int, input().split()))

picks = list(combinations(cows, M))

answer = set()
for pick in picks:
    sums = sum(pick)
    if is_Prime(sums):
        answer.add(sums)
if len(answer) >= 1:
    answer = list(answer)
    answer.sort()
    print(*answer)
else:
    print(-1)


'''
이거 
1 1
1 
입력하면 1 나오는 멍청 코딩입니다. 
이걸 통과시키네
'''
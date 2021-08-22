'''
접근 : 투포인터
'''
import sys
from collections import Counter
input = sys.stdin.readline

# 총 인형 수, 필요 인형 수(키로 쓰게 문자열로 받음)
N, M = map(int,input().split())
dolls = list(input().split())

# 애초에 인형은 충분한가
if M > dolls.count('1'):
    print(-1)
    exit(0)

# 풀이 시작
need = Counter()
need['1'] = M
left = start = end = 0

# 오른쪽 포인터 이동
for right, doll in enumerate(dolls, 1):   # enumerate를 저렇게 쓰면 1부터 시작함
    # 오른쪽 포인터 이동하면서 확인 확인
    if need[doll] > 0:
        M -= 1
    need[doll] -= 1

    # 네 0! 왼쪽 포인터의 이동을 판단한다.
    if M == 0:  
        while left < right and need[dolls[left]] < 0:  
            need[dolls[left]] += 1
            left += 1
        # 다 끝나고 한번 더                    
        need[dolls[left]] += 1                  
        M += 1   

        # 윈도우 업데이트
        if end == 0 or right-left < end-start:  
            start, end = left, right
        left += 1  
# 없을 경우, -1 출력
if M == 1:
    print(end-start)
else:
    print(-1)

'''
투 머치 풀이
1. 일단 탐색 종류가 하나면 카운터 쓸 필요 없음
2. 보면 알겠지만 end랑 start는 굳이 저렇게 저장할 필요 없었음.
>>> 모든건 확장성을 위하여 + 대는 소를 겸한다.
'''
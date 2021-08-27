'''
삼성 IM 역량테스트와 매우 유사한 문제라고 한다.
'''

import sys
input = sys.stdin.readline

# 스위치 수, 스위치 상태
N = int(input())
switches = list(map(int, input().split()))

for _ in range(int(input())):
    # 1이 남자, 2가 여자
    gender, order = map(int, input().split())
    # 남자
    if gender == 1:
        i = order - 1
        while(i <= N - 1):
            switches[i] ^= 1
            i += order
    # 여자
    else:
        order = order - 1
        switches[order] ^= 1
        i = 0
        while True:
            i = i + 1
            if order + i <= N - 1 and order - i >= 0:
                if switches[order-i] == switches[order+i]:
                    switches[order+i] ^= 1
                    switches[order-i] ^= 1
                else:
                    break         
            else:
                break

# 이상한 출력 형식
for i in range(0, N, 20):
    print(*switches[i:i+20])
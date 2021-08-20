'''
접근: N이 99, 날짜가 7 log100이 6.x인 시점에서 무언가를 나누라는건 알 수 있다. 무얼 나누지.
AAAA BBB
AA BB AA B
A B A B A B B
완벽히 이해했다.
'''

import sys
input = sys.stdin.readline

# 변수 : X일차, 인덱스만 보내기
def divide(days, l, r):
    # 1 or 2까지 쪼개기 no 7일까지 쪼개기
    if days == 8:
        return None
    if l>r:
        l = r
    # 분할
    idx = (l+r)//2

    # 정복(좌측을 바꾼다)
    for i in range(l, idx+1):
        if answers[days-1][i] == 'A':
            answers[days][i] = 'B'
        else:
            answers[days][i] = 'A'
    # 정복(우측을 유지한다.)
    for i in range(idx+1,r+1):
        answers[days][i] = answers[days-1][i]

    divide(days+1, l, idx)
    divide(days+1, idx+1, r)



N = int(input())
answers = [['A']*N for _ in range(8)]

divide(1,0,N-1)

for i in range(1,8):
    print(''.join(answers[i]))
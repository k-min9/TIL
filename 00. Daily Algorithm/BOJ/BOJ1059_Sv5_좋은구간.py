'''
메모장 적는 시간이 코딩하는 시간보다 길어지는 타입의 문제
'''

import sys
input = sys.stdin.readline

L = int(input())
S = [0] + list(map(int, input().split()))  # 혹시 했는데 0 안넣어서 안 풀린거였음
n = int(input())


# 마지막 예제 보면 아는데 중복이면 안됨 하...
S.sort()

answer = 0

for i in range(1,L+1):
    if S[i-1]<n<S[i]:
        a = S[i-1] + 1
        b = S[i] - 1
    else:
        continue
    answer = answer + (b-a)  # n 자체를 포함
    answer = answer + (n-a)*(b-n)  # 미만 숫자와 초과 숫자의 조합

print(answer)

'''
문제 잘못이해해서 한번 틀림 엌ㅋㅋ 
근데도 변수 선언한거 귀찮아서 숫자도 안 고침 엌ㅋㅋ
하... 아침부터 뭐하냐 나
'''

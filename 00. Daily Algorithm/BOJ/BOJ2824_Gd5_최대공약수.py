import sys
input = sys.stdin.readline
from math import gcd

input()
A_list = map(int, input().split())
input()
B_list = map(int, input().split())

A, B = 1, 1
for i in A_list:
    A *= i
for i in B_list:
    B *= i

answer = gcd(A, B)
if answer >= 1000000000:
    print(str(answer)[-9:])
else:
    print(answer)

'''
정답률 22%...
파이썬은 숫자 21억 넘어가도 그냥 계산하니까 괜찮으려나 했더니 진짜로 괜찮았다...
오버플로우를 전혀 고려하지 않아도 되는 파이썬 한정으로 골드가 아닌 브론즈 문제
씨플플이면 아마 소인수분해로 풀었을듯
'''

'''
감상 : 여태 풀던 숨바꼭질 시리즈(1~5)와 무관.
아니 그냥 최대공약수 구하는 문젠데 이거
'''

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
bros = list(map(int, input().split()))

for i in range(N):
    bros[i] = bros[i] - S

import math
print(math.gcd(*bros))

'''
숨바꼭질 축제의 마무리로는 허전하다;;; 
누구임 이름 끝에 6 붙인 사람
'''
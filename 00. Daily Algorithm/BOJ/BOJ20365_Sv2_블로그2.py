'''
스터디 코드 리뷰 + 리팩토링
'''

import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()
cnt = {'B': 0,'R': 0}
cnt[s[0]] += 1
for i in range(1,N):
    if s[i] != s[i-1]:
        cnt[s[i]] += 1
print(min(cnt['B'],cnt['R'])+1)

'''
요즘 flag 처리로 문제 많이 푸는데 이거가 딱 그런 느낌
N이 50만에 색이 2개여서, N이 100에 색이 3개인 16157_블로그와는 거의 다른 문제
'''
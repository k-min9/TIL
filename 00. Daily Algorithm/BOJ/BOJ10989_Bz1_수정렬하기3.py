'''
N이 천만 이하고, 숫자가 만 이하면 이건 정렬을 하라는 소리가 아니다
'''
import sys
input = sys.stdin.readline

N = int(input())

num = [0] * 10001

for _ in range(N):
    temp = int(input())
    num[temp] += 1
    
for i in range(10001):
    if num[i]:
        for j in range(num[i]):
            print(i)

'''
제목사기
'''
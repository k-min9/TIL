'''
n보다 작은 모든 서로소 구하기
= 오일러 피 함수를 직접 코딩해봐라
'''
import sys
input = sys.stdin.readline

N = int(input())
answer = N
 
for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        while N % i == 0:
            N //= i
 
        answer -= answer / i
 
if N > 1:
    answer -= answer / N
 
print(int(answer))

'''
갑자기 분위기 수학공부
'''
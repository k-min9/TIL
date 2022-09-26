'''
초등학교 문제! 5의 배수!
'''
import sys
input = sys.stdin.readline

N = int(input())

answer = 0
while N != 0:
    N //= 5
    answer += N
print(answer)

'''
고유한 번호 = 난이도 폭락
'''
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
check = set(map(int, input().split()))

answer = 0
for c in check:
    if M-c in check:
        answer += 1
print(answer//2)

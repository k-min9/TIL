'''
이 문제는 뭐가 하고 싶었던 걸까
'''
import sys
input = sys.stdin.readline

# 배열 수, 첫 항, 공차
N, A, D = map(int, input().split())
nums = list(map(int,input().split()))

answer = 0
for num in nums:
    if num == A:
        answer += 1
        A += D

print(answer)
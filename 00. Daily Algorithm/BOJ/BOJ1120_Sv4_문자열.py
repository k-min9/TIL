'''
윈도우마냥 한번 쓱 긁으면 끝나겠는데
'''
import sys
input = sys.stdin.readline

A, B = input().split()

answer = 987654321
for i in range(len(B) - len(A) + 1):
    count = 0
    for j in range(len(A)):
        if A[j] != B[i+j]:
            count += 1
    answer = min(answer, count)

print(answer)
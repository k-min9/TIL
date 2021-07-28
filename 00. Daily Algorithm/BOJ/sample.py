# 기본 전처리
import sys
input = sys.stdin.readline

result = 1
while result:
    A, B = map(int, input().split())
    result = A + B
    print(result)
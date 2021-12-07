'''
스택쓰고, 여는 괄호와 닫는 괄호 위치 저장
'''
import sys
input = sys.stdin.readline

S = list(input())
left, right, total, sol = 0, 0, 0, 0

for b in S:
    if b == '(':
        left += 1
        total += 1
    else:
        right += 1
        total -= 1
    
    if total <= 1: # 지금까지의 (은 바꿀 수 없음
        left = 0
    
    if total == -1: # )이 1개 더 많아지는 순간 지금까지의 모든 ) 바꿀 수 있음
        sol = right # 오타는 하나 뿐 = 문제 없음
        break

if total > 0:
    sol = left
print(sol)
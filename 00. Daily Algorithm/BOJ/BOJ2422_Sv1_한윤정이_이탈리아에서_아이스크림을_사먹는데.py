'''
숫자가 작음 = 머리를 안씀
N이 32가 넘어갈때 비트마스킹하면 뭐가 일어나는지 구경이나 하자
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
worsts = set()
for _ in range(M):
    a, b = map(int, input().split())
    worst = 1<<(a-1)
    worst |= 1<<(b-1)
    for i in range(N):
        worsts.add(bin(worst|(1<<i)))

cnt = 0        
for worst in worsts:
    if worst.count('1') == 3:
        cnt = cnt + 1

print(N*(N-1)*(N-2)//6 - cnt)

'''
역시 숫자가 너무 작아서 통과됨.
아무일도 안일어난다. 
파이썬은 비트마스크 연산 제한 없음 이란걸 배움 끝
'''
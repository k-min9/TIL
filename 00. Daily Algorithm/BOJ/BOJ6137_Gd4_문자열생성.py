'''
문자열 제어가 요즘 많긴 하네...
투포인터로 제어, 심지어 파이썬 문자열끼리 대소구분도 가능...
'''
import sys
input = sys.stdin.readline
N = int(input())
S, T = '', ''
for _ in range(N):
    s = input().rstrip()
    S += s
 
cnt = 0
i, j = 0, N-1
while i <= j:
    if S[i] < S[j]:
        T += S[i]
        i += 1
    elif S[i] > S[j]:
        T += S[j]
        j -= 1
    # 같을 경우... 그 안에서 또 새 포인트를 사용
    else:
        ii, jj = i, j
        diff = False
        while ii <= jj:
            if S[ii] < S[jj]:
                T += S[i]
                i += 1
                diff = True
                break
 
            elif S[ii] > S[jj]:
                T += S[j]
                j -= 1
                diff = True
                break
 
            else:
                ii += 1
                jj -= 1
            
        if not diff:
            T += S[i]
            i += 1
 
    cnt += 1
    # 80줄마다 새 줄 문자
    if cnt % 80 == 0:
        T += '\n'
 
print(T)

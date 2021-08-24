import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    A, B = input().split()
    ans = A.split(B)

    print(f'#{t + 1}', len(A) - (len(ans)-1)*(len(B)-1))

import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())
    answer = [0]*N
    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            answer[j] = i

    print(f'#{t}', *answer)

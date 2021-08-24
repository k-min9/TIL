import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    A = input().rstrip()
    B = input().split(A)
    answer = 0
    if len(B) != 1:
        answer = 1

    print(f'#{t + 1}', answer)

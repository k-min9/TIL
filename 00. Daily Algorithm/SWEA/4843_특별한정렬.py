import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    N = int(input())
    answer = [0]*10
    numbers = list(map(int,input().split()))
    numbers.sort()
    numbers_special = numbers[N//2:]
    numbers_special.sort(reverse=True)

    N = N//2
    for i in range(5):
        answer[2*i+1] = numbers[i]
    for i in range(5):
        answer[2*i] = numbers_special[i]

    print(f'#{tc + 1}', *answer)

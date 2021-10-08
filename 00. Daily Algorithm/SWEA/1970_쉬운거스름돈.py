import sys
sys.stdin = open('input.txt')

# 상수
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(int(input())):
    money = int(input())
    answers = [0] * 8

    for i in range(8):
        answers[i] = money//coins[i]
        money = money % coins[i]

    print(f'#{tc+1}')
    print(*answers)

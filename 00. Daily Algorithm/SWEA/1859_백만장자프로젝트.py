import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    # 총 이익, 매수각
    ans = 0
    sell_time = prices[-1]
    # 미래에서 현재로 오면 바로 알 수 있다.
    while prices:
        price = prices.pop()
        ans += max(sell_time - price, 0)
        sell_time = max(sell_time, price)

    print(f'#{t+1}', ans)

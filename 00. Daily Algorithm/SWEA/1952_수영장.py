import sys
sys.stdin = open('input.txt')


for t in range(int(input())):
    # 가격 설정(일, 월, 3개월, 1년)
    p1, p2, p3, p4 = map(int, input().split())
    plans = list(map(lambda x: int(x)*p1, input().split()))

    dp = [0]*13
    for i in range(1, 13):
        dp[i] = dp[i-1] + min(plans[i-1], p2)
        if i > 2:
            dp[i] = min(dp[i], dp[i-3] + p3)

    print(f'#{t+1}', min(dp[12], p4))

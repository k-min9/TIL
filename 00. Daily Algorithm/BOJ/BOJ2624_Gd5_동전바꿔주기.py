'''
2차원 dp로 풀면 좋아보이지만 그렇지 않은 문제
큰 동전순으로 돌아가면서 각 동전마다 역으로 체크를 하게 되면, 
예제 같은 경우는 10*2, 10*1에 1씩 기록, 5가 10*1기록에 5*2를 추가하며 기록... 하면서 4개의 결과가 나온다.
'''
T = int(input())
k = int(input())
 
money = [list(map(int,input().split())) for _ in range(k)]
 
money.sort(reverse=True)
dp = (T+1)*[0]
 
dp[0] = 1
for coin_val, coin_cnt in money:
    for current_money in range(T,1,-1):
        for current_cnt in range(1,coin_cnt+1):
            if current_money - current_cnt*coin_val >= 0:
                dp[current_money] += dp[current_money-current_cnt*coin_val]

print(dp[T])
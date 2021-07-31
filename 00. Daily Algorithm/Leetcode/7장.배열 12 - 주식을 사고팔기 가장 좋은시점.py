# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# 풀이 1: One pass (저점과 현재값의 차이 누적)

def maxProfit(self, prices: list[int]) -> int:
    profit = 0
    min_price = 1e9
    
    #최소 최대 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    
    return profit
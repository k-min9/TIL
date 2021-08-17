# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 풀이 2 : 여러번 팔 수 있는 시점부터 전보다 문제가 쉬워지는데, 올라갈때마다 팔면 끝이다

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i+1] - prices[i], 0) for i in range(len(prices)-1))
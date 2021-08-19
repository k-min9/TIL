# https://leetcode.com/problems/climbing-stairs
# 풀이 : 기본 DP (피보나치 청개구리짓)

class Solution:
    def climbStairs(self, n):
        a, b = 1,0
        for _ in range(n):
            a, b = a+b, a
        return a
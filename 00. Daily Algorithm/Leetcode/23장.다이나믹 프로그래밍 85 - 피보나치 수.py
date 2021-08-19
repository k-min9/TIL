# https://leetcode.com/problems/fibonacci-number
# 풀이  : 기초적인 DP

import collections

class Solution:
    dp = collections.defaultdict(int)
    
    def fib(self, N):
        self.dp[1] = 1
        
        for i in range(2,N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[N]
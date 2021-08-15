# https://leetcode.com/problems/number-of-1-bits
# 풀이  : 비트연산 : 연산할때마다 맨 오른쪽 비트가 빠짐!

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        
        while n:
            #연산한번하면 1011이 1010이 되는 식으로 맨 오른쪽 1이 사라짐
            n = n & (n-1)
            cnt = cnt + 1
        return cnt
        
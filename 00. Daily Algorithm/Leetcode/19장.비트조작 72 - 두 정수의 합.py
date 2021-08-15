# https://leetcode.com/problems/sum-of-two-integers
# 풀이 2 : 2의 보수, 작동원리 확실히 봐두자. 아니 봤는데 잊은거긴 한데.

class Solution(object):
    def getSum(self, a, b):

        mask = 0xffffffff
        while b:
            # 더한 값과 올라가는 수
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry

        # 음수처리 안하면 -20을 20억으로 인식한다.
        if (a>>31) & 1:
            return ~(a^mask)
        return a
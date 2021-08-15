# https://leetcode.com/problems/hamming-distance
# 풀이  : XOR을 이용해서 처리

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
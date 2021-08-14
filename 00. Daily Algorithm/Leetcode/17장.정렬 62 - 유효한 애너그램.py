# https://leetcode.com/problems/valid-anagram
# 풀이 1 : 소트는 위대해

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
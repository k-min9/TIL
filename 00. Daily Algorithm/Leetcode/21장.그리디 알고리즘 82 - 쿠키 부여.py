# https://leetcode.com/problems/assign-cookies
# 풀이  : 소트해서 하나씩 일치하면 끝

class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
# https://leetcode.com/problems/merge-intervals
# 풀이 1 : 구간 병합

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged = []
        for i in sorted(intervals):
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += [i]
        return merged

'''
merged += i,
merged += [i]
merged.append(i)
같은 표현이지만 후자가 걍 제일 빠르다 이상한 짓 하지 말자
'''
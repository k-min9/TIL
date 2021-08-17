# https://leetcode.com/problems/queue-reconstruction-by-height
# 풀이 X : 우선순위 큐 소개 >> 아니 한번만 하면 되는데 정렬하면 되지

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return people
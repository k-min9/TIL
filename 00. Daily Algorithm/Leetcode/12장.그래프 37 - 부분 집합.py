# https://leetcode.com/problems/subsets
# 풀이 X: 아니 itertools 쓰세요...;

import itertools
# 구현의 효율성, 성능을 위하여 허락된 라이브러리를 사용하였다.

def subsets(self, nums: list[int]) -> list[list[int]]:
    answer = []
    for i in range(len(nums)+1):
        answer += list(map(list,itertools.combinations(nums,i)))

    return answer   
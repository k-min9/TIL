# https://leetcode.com/problems/permutations
# 풀이 2: 저는 itertools가 좋아요. itertools 구현은 c라이브러리 

import itertools
# 구현의 효율성, 성능을 위하여 허락된 라이브러리를 사용하였다.

def permute(self, nums: list[int]) -> list[list[int]]:
    return list(map(list,itertools.permutations(nums)))

    # map 안하면 [(1,2,3), (1,3,2)] 이런식으로 내용물이 tuple
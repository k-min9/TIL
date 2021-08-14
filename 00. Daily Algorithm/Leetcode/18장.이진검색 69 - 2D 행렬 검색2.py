# https://leetcode.com/problems/search-a-2d-matrix-ii
# 풀이 2 : 파이써닉

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return any(target in row for row in matrix)

'''
풀이 1이 더 중요하긴 함, 우측상단에서 시작해서 크면 아래 한칸 작으면 왼쪽 한칸
'''

# 풀이 3 : 2차원 배열을 1차원 배열로!

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 예술적
        matrix = set(j for i in matrix for j in i)
        return target in matrix

# 풀이 4 : 하나 더!
import itertools
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 예술적
        matrix = set(itertools.chain(*matrix))
        return target in matrix
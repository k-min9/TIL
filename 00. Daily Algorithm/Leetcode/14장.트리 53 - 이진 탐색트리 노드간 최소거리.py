# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# 풀이 2 : 반복구조 중위 순회 (좌부모우)

import sys

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        
        # 반복구조 중위 순회 비교 결과
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
                
            node = stack.pop()
            
            result = min(result, node.val - prev)
            prev = node.val
            
            node = node.right
            
        return result
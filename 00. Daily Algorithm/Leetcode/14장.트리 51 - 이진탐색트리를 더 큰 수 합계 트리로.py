# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
# 풀이 : 이진탐색트리면 오른쪽 끝이 가장 큰 수. 여태 누적값+현재값으로 계산

class Solution:
    val = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        
        # 솔루션 프로그램 특징
        return root
# https://leetcode.com/problems/range-sum-of-bst
# 풀이 0: 왜 L과 R을 안움직이고?? 투 포인터로 해결

class Solution:
    s = 0
    def rangeSumBST(self, root: Optional[TreeNode], L: int, R: int) -> int:

        def check(root, L, R):
            if L<=root.val<=R:
                self.s += root.val
            if root.left and L<root.val:
                check(root.left, L, R)
            if root.right and R>=root.val:
                check(root.right, L, R)

        check(root, L, R)
        return self.s
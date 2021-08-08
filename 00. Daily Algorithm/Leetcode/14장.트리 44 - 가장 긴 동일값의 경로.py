# https://leetcode.com/problems/longest-univalue-path/
# 풀이 : 43과 유사한 문제, DFS로 풀이

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = 0
    
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드와 자식 노드가 일치하는지 판별
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
            self.result = max(self.result, left+right)

            # 자식중 큰 쪽 리턴
            return max(left,right)
    
        dfs(root)
        return self.result
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# 풀이 : 전위 순회 결과로 중위 순회 분할 정복

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            # 전위 순회 결과로 중위 순회 분할 인덱스
            idx = inorder.index(preorder.pop(0))
            
            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[idx])
            node.left = self.buildTree(preorder, inorder[0:idx])
            node.right = self.buildTree(preorder, inorder[idx+1:])
            
            return node
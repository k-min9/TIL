# https://leetcode.com/problems/invert-binary-tree
# 풀이 2 : BFS로 순회 반전

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    q =collections.deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        # 부모에서 자식으로 스왑
        if node:
            node.left, node.right = node.right, node.left
            
            q.append(node.left)
            q.append(node.right)
            
    return root

'''
풀이 1 : 파이써닉 풀이
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None
'''
# https://leetcode.com/problems/merge-two-binary-trees
# 풀이 : 재귀 탐색

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        return node
    return t1 or t2

'''
트리 병합이 내용물 잇는건줄 알았더니 그냥 더하기 였어 하..........
'''
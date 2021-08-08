# https://leetcode.com/problems/maximum-depth-of-binary-tree
# 풀이 : BFS 탐색

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    
    q = collections.deque()
    q.append(root)
    depth = 0
    
    while q:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(q)):  # 부모 노드 이상의 서치는 없다.
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
                
    return depth
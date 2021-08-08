# https://leetcode.com/problems/diameter-of-binary-tree
# 풀이 : DFS 풀이

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    longest = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: TreeNode):          
            if not node:
                return -1
            
            # 왼쪽 오른쪽 각 리프노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left+right+2)
            
            # 상태값
            return max(left, right) + 1
        
        
        dfs(root)
        return self.longest


'''
처음으로 클래스 변수 사용
중첩함수는 부모함수의 변수에 재할당을 할 수 없고, 로컬로 선언해버린다. 그래서 사용.
'''
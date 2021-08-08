# https://leetcode.com/problems/serialize-and-deserialize-binary-tree
# 풀이 : BFS로 구현

import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        q = collections.deque()
        q.append(root)
        result = ['#']
        
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)        

    def deserialize(self, data):
        # 예외 처리
        if data == '# #':
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        q = collections.deque()
        q.append(root)
        index = 2
        
        # 자식노드 결과 확인 후 큐 삽입
        while q:
            node = q.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                q.append(node.left)
            index = index + 1
            
            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                q.append(node.right)
            
            index = index + 1
        
        return root
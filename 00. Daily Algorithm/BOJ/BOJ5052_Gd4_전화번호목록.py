'''
문자열 비교
1. 소팅하면 i번째와 i+1번째를 비교해도 앞 부분이 비슷한지 확인할 수 있다.
2. 트라이 쓰자 트라이 >> 이걸로 진행
3. zip과 startswith 섞어서 체크
'''
import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.child = {}
        
class Trie(object):
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, string):
        curr_node = self.root
        
        for s in string:
            if s not in curr_node.child:
                curr_node.child[s] = Node(s)
            curr_node = curr_node.child[s]
        
        curr_node.data = string
        
    def search(self, string):
        curr_node = self.root
        
        for s in string:
            curr_node = curr_node.child[s]
            
        if curr_node.child:
            return False
        else:
            return True

t = int(input())
for _ in range(t):
    n = int(input())
    trie = Trie()
    nums = list()
    for _ in range(n):
        num = input().rstrip()
        nums.append(num)
        trie.insert(num)
    
    flag = True
    nums.sort()
    for num in nums:
        if not trie.search(num):
            flag = False
            break
    if flag:
        print('YES')
    else:
        print('NO')
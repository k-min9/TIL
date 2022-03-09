'''
언젠가는 풀어야지 했던 트라이문제
'''
import sys
input = sys.stdin.readline

class Node(object):
    # 해당 노드의 문자, 자식들, 문자의 끝인지 체크
    def __init__(self, value):
        self.value = value
        self.child = {}
        self.chk = False
        
class Trie(object):
    def __init__(self):
        self.root = Node(None)
        
    def insert(self, string):
        curr_node = self.root
        
        for s in string:
            # 해당 노드의 자식들에 그 문자가 없으면
            if s not in curr_node.child:
                # 새로운 노드 생성
                curr_node.child[s] = Node(s)
            # 그리고 이어주기
            curr_node = curr_node.child[s]
        
        # curr_node.value = string
        curr_node.chk = True
        
    # 해당 문제용 search
    def search(self, string):
        cnt = 0
        curr_node = self.root

        # 해당 노드 자식이 둘 이상이거나, 아직 끝이 아닐경우 이어짐
        for s in string:
            curr_node = curr_node.child[s]
            if len(curr_node.child)>1 or curr_node.chk:
                cnt+=1
        return cnt


while True:
    t = Trie()

    try:
        N = int(input())
    except:
        break
    words = [input().strip() for _ in range (N)]

    # 트라이 작성
    for word in words:
        t.insert(word)
    
    # 정답!
    answer = 0
    for word in words:
        answer += t.search(word)
    print("%.2f" %(answer/N))

'''
트라이 최대 단점 : 샘플 문제가 적음!
오늘도 조금 더 똑똑해졌당!
'''
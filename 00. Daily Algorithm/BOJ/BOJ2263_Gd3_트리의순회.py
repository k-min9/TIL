'''
프리(Pre)오더 : RootLR > 전위 >>>> DFS
인(In)오더 : LRootR > 중위
포스트(Post)오더 : LRRoot : 후위 >>>> 
'''
# 전위, 중위 순회 결과로 이진 트리 구축 by 파이썬 알고리즘 테스트
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def pre_order(in_order, post_order):
    # 받은 트리가 비어있음
    if not post_order:
        return
    
    # 후위의 맨 마지막이 루트(전위의 맨 앞)
    root = post_order.pop()
    index = in_order.index(root)
    preorder.append(root)
    #print(preorder)

    # 서브트리 분할
    left_inorder = in_order[:index]
    right_inorder = in_order[index+1:]
    left_postoder = post_order[:index]
    right_postorder = post_order[index:]

    # 순차 호출
    pre_order(left_inorder, left_postoder)
    pre_order(right_inorder, right_postorder)

# pre_order의 인덱스 버전
def pre_order2(in_start, in_end, post_start, post_end):
    # 받은 트리가 비어있음
    if in_start > in_end: #or post_start > post_end: 
        return 

    # 후위의 맨 마지막이 루트(전위의 맨 앞)
    root = postorder[post_end] 
    preorder.append(root)

    # 서브트리 분할
    left = pos[root] - in_start 
    right = in_end - pos[root] 
    pre_order2(in_start, in_start+left-1, post_start, post_start+left-1)
    pre_order2(in_end-right+1, in_end, post_end-right, post_end-1)


# 트리 길이
N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
preorder = []

# 해당 노드의 in-order에서의 위치
# 2차 시도 풀이에서 제일 난이도 높은 핵심파트였음
# 이걸 N+1에 넣어서 이렇게 만들 생각한 사람 천재가 틀림없다.
pos = [0]*(N+1)
for i in range(N):
    pos[inorder[i]] = i
# print(pos)

# pre_order(inorder, postorder)
pre_order2(0, N-1, 0, N-1)
print(*preorder)

'''
1차 시도: 메모리 초과
2차 시도: 인덱스만 보내라
'''
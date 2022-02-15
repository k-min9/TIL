'''
LCA라 불리는 웰노운 알고리즘이라고 한다.
뭐 내용은 그냥 단순 parent긴 하던데...
오늘도 바빠서 코드 학습만! 프로젝트 마지막주 파이팅!!
'''
import sys
input = sys.stdin.readlin

T = int(input())

# 입력과, 부모노드
for _ in range(T):
    N = int(input())
    p_list = [0 for _ in range(N+1)]      
    for _ in range(N-1):
        p,c = map(int, input().split())
        p_list[c] = p                     #부모 노드 저장
 
    a,b=map(int,sys.stdin.readline().split())
    

    a_parent = [a]
    b_parent = [b]
    while p_list[a]:
        a_parent.append(p_list[a])
        a=p_list[a]
    while p_list[b]:
        b_parent.append(p_list[b])
        b=p_list[b]
 
    a_level=len(a_parent)-1
    b_level=len(b_parent)-1

    #부모노드가 같지 않을때까지
    while a_parent[a_level]==b_parent[b_level]:   
        a_level-=1
        b_level-=1
 
    print(a_parent[a_level+1])
'''
세그먼트 트리 강화 구간
'''
import sys
input=sys.stdin.readline


# 세그먼트 트리 생성
def init(start,end,index):
    if start==end:
        tree[index]=arr[start]
    else:
        mid=(start+end)//2
        tree[index]=min(init(start,mid,index*2),init(mid+1,end,index*2+1))
    return tree[index]

def update(start,end,index,w,v):

    # 범위 체크
    if start>w or end<w:
        return 

    # 자식 노드에 최소값 부여
    if start==end:
        tree[index]=v
        return

    mid=(start+end)//2
    update(start,mid,index*2,w,v)
    update(mid+1,end,index*2+1,w,v)
    tree[index]=min(tree[index*2], tree[index*2+1])
        
# 최소값 찾기
def find_min(start,end,index,left,right):
    if start>right or end<left:
        return [sys.maxsize,sys.maxsize]
    if start>=left and right>=end:
        return tree[index]
    mid=(start+end)//2
    return min(find_min(start,mid,index*2,left,right), find_min(mid+1,end,index*2+1,left,right))


N=int(input())
arr=[]
tmp=list(map(int,input().split()))
for i in range(N):
    arr.append([tmp[i],i+1])
tree=[0]*(N*4)  # 노드 값 = 최소값

init(0, N-1, 1)
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    if a==1:
        arr[b-1][0]=c
        update(0, N-1, 1, b-1, arr[b-1])
    elif a==2:
        print(find_min(0, N-1, 1, b-1, c-1)[1])


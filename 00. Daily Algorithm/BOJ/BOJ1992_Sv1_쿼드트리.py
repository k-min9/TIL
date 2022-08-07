'''
~분할정복 Festival~ 2/10
'''
import sys
input = sys.stdin.readline

N = int(input())
graphs = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def divide_tree(num, tree) :
    # 압축 가능 여부
    check = 0
    for i in range(num) : 
        check += sum(tree[i]) # 동영상의 모든 수의 합
    
    if check == 0 : # 0으로 압축
        print(0,end='') 
    elif check == num*num : #1로 압축
        print(1,end='') 
    else: # 압축이 불가
        print('(',end='')
        temp = [tree[i][0:num//2] for i in range(0,num//2)] # 4개로 나눠서 순서대로 앞 과정 반복
        divide_tree(num//2,temp)
        temp = [tree[i][num//2:num] for i in range(0,num//2)] 
        divide_tree(num//2,temp)
        temp = [tree[i][0:num//2] for i in range(num//2,num)] 
        divide_tree(num//2,temp)
        temp = [tree[i][num//2:num] for i in range(num//2,num)] 
        divide_tree(num//2,temp)
        print(')',end='')

divide_tree(N, graphs)

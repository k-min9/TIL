'''
전위, 중위 주어지고 후위 맞추기
'''
import sys
input = sys.stdin.readline


def solve(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:
            # 여기서 왼쪽은 좌측 트리
            solve(root+1, start, i)
            # 나머지는 우측 트리
            solve(root + i + 1 - start, i + 1, end)
            # 출력시 자동 후위가 나옴
            print(inorder[i], end=' ')


for _ in range(int(input())):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solve(0, 0, N)
    print()
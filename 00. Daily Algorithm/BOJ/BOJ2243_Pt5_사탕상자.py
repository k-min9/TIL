'''
2면 사탕 넣기
1이면 사탕 꺼내기
태그 : 세그먼트 트리
'''
import sys
input = sys.stdin.readline


# 트리 세팅
def init(n, s, e, t, v):
    if t < s or e < t:
        return tree[n]
    
    if s == t == e:
        tree[n] += v
        arr[n] = t
        return tree[n]
    
    m = (s + e) // 2
    tree[n] = init(n * 2, s, m, t, v) + init(n * 2 + 1, m + 1, e, t, v)

    return tree[n]

def get(n, s, e, g):
    if (s == e):
        tree[n] -= 1
        print(arr[n])
        return tree[n]

    l = tree[n * 2]
    m = (s + e) // 2
    # 왼쪽으로 갈지 오른쪽으로 갈지
    if l >= g:
        get(n * 2, s, m, g)
    else:
        get(n * 2 + 1, m + 1, e, g - tree[n * 2])

    tree[n] = tree[n * 2] + tree[n * 2 + 1]

    return tree[n]

N = int(input())
tree = [0] * (1000000 * 4)
arr = [0] * (1000000 * 4)  # index 용

for _ in range(N):
    cmd = list(map(int, input().split()))
    # 빼기
    if cmd[0] == 1:
        get(1, 1, 1000000, cmd[1])
    # 넣기
    elif cmd[0] == 2:
        init(1, 1, 1000000, cmd[1], cmd[2])

'''
오랜만에 클래스 문제! (10868로 연습 한 번 더 가능)
최솟값과 최대값을 담는 세그먼트 트리를 만들고
초기화, 최솟값 검색 최댓값 검색을 하자
참고 : https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-2357-%EC%B5%9C%EC%86%9F%EA%B0%92%EA%B3%BC-%EC%B5%9C%EB%8C%93%EA%B0%92
'''
import sys
input = sys.stdin.readline
import math

sys.setrecursionlimit(10 ** 8)

# 세그먼트 트리 만들기
def make_seg(idx, start, end):

    # 리프 노드
    if start == end:
        seg[idx] = (arr[start], arr[start])  # min, max
        return seg[idx]

    mid = (start + end) // 2

    l = make_seg(idx * 2, start, mid)
    r = make_seg(idx * 2 + 1, mid + 1, end)

    seg[idx] = (min(l[0], r[0]), max(l[1], r[1]))
    return seg[idx]

# 탐색범위 start ~ end
def find(start, end, idx):

    # 찾으려는 범위와 전혀 겹치지 않음
    if end < a or b < start:
        return (1000000000, 0)

    mid = (start + end) // 2

    # 찾으려는 범위가 트리 범위에 속함
    if a <= start and end <= b:  # 탐색 범위가 작아서 다 리턴
        return seg[idx]

    else:
        l = find(start, mid, idx * 2)
        r = find(mid + 1, end, idx * 2 + 1)
        return (min(l[0], r[0]), max(l[1], r[1]))  # 최대값끼리, 최소값끼리


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

b = math.ceil(math.log2(N)) + 1  # 트리 높이
node_n = 1 << b
seg = [0] * node_n

make_seg(1, 0, len(arr) - 1)

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  # idx
    ans = find(0, len(arr) - 1, 1)
    print(ans[0], ans[1])

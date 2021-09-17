'''
이진탐색이라고 생각했는데 N = 1000이요??
'''

# import sys
# input = sys.stdin.readline

# N, height = map(int, input().split())
# fruits = list(map(int, input().split()))

# fruits.sort()

# answer = 0
# lo, hi = 0, N-1
# while lo < hi:
#     mid = (lo + hi) // 2
#     if fruits[mid] <= height + mid:
#         lo = mid + 1
#         answer = lo
#     else:
#         hi = mid

# if fruits[answer] <= height + answer:
#     answer += 1

# print(height + answer)
'''
으디서 실수한겨;;; N 낮으니까 무지성 2회차
'''

import sys
input = sys.stdin.readline

N, height = map(int, input().split())
fruits = list(map(int, input().split()))

fruits.sort()

for fruit in fruits:
    if fruit <= height:
        height += 1
    else:
        break

print(height)
'''
투 포인터 해야되는데 이거 되나 했더니 되버렸다.
'''

import sys
input = sys.stdin.readline

# 소의 수, 코스튬의 크기
N, S = map(int, input().split())
cows = list()
for _ in range(N):
    cows.append(int(input()))
cows.sort()

answer = 0
for left in range(N-2):
    for right in range(N-1, left, -1):
        if cows[left] + cows[right] <= S:
            answer += right-left
            break
print(answer)

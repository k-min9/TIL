'''
가로냐 세로냐 그것이 문제로다 >> 비트마스킹
제가 비트마스킹을 그닥 안 좋아하는건 기껏해야 32자리 내의 임금님이기 때문입니다.
아니 애초에 비트마스킹 하고 싶으면 C나 쓰라구...
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boxes = [list(map(int, input.split()))]

answer = 0
for i in range(1 << N*M):
    sums = 0
    for i in range(N):

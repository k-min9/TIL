'''
지나가야하는 방의 개수 1개 : 1
지나가야하는 방의 개수 2개 : 2 ~ 7 (+6)
지나가야하는 방의 개수 3개 : 8 ~ 19 (+12)
지나가야하는 방의 개수 4개 : 20 ~ 37 (+18)
지나가야하는 방의 개수 5개 : 38 ~ 61

초등학교 수학으로 변하는 순간이지만 귀찮으니 컴퓨터를 굴리겠다
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

cnt = 1
cnt_six = 6
answer = 1

while N > cnt:
    answer += 1
    cnt += cnt_six
    cnt_six += 6
print(answer)

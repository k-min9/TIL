'''
구... 현인가?
'''
import sys
input = sys.stdin.readline
from collections import defaultdict

# 벨트위 접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = map(int, input().split())
susi = [int(input()) for _ in range(N)]

l = 0
r = 0
dict = defaultdict(int)
answer = 0

# 우선 k 만큼 먹기
while r < k:
    dict[susi[r]] += 1
    r += 1

# 공짜 초밥 먹기
dict[c] += 1

# 슬라이딩 윈도우
while l < N:
    answer = max(answer, len(dict))

    dict[susi[l]] -= 1  # 맨 왼쪽 초밥 제거
    if dict[susi[l]] == 0: del dict[susi[l]]  # defaultdict라 0 직접 제거
    dict[susi[r%N]] += 1

    l += 1
    r += 1

print(answer)

'''
한바퀴 돌면 대략 O(N)*O(k)... 맞지?
'''
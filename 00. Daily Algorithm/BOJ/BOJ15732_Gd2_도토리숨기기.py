'''
문제 이해가 더 어려웠던 문제;;;
예제 좀 더 주지...
전부 쭉 하게 되면 상자수*규칙수(N*K) 만큼 해야되지만, 이분탐색이면 NlogN으로 처리 가능
'''
import sys
input = sys.stdin.readline

# 상자 수, 규칙 수, 도토리 갯수
N, K, D = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(K)]

# 그 지점까지의 도토리 수
def calc(idx):
    total = 0
    for start, end, step in rules:
        if start <= min(end, idx):
            total += (min(end, idx) - start) // step + 1
    return total

lo, hi = 1, 1000000

answer = 0
while lo <= hi:
    mid = (lo + hi) // 2

    if calc(mid) >= D:
        answer = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(answer)















'''
도토리가 왜 Acorn의 A가 아니고 D인지가 더 궁금한 문제 혹시 Dotori나 Donguri 인가...?
'''
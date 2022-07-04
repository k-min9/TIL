'''
요즘 먼가 이분 탐색 문제가 많이 나오네
'''
import sys
input = sys.stdin.readline


# 박스 수, 가로세로높이
N, L, W, H = map(int, input().split())
S, E = 0, max(L, W, H)

for _ in range(10000):
    M = (S + E) / 2
    count = (L // M) * (W // M) * (H // M)
    if count >= N:
        S = M
    else:
        E = M

# 오차 -10^9
print("%.10f" %(E))

'''
O(NlogN)까지 세이프
우선 K(K-1)//2보다 N이 작으면 -1, 그 외에는 어떻게든 된다.
'''
import sys 
input = sys.stdin.readline

# 플레이어 수, 팀 수
N, K = map(int, input().split())

if N < K*(K+1)//2:
    print(-1)
    exit(0)

# 흠???
N -= K*(K+1)//2
if N%K == 0:
    print(K)
else:
    print(K-1)

'''
아니 이거 단순한 수학 문제잖아;;;;;;;
O(1)
'''
'''
0 1 2 3 4 5 6
1 1 2 3 3 2 1
먼가 한 줄 식 있겠지만 빡빡한 문제도 아니고 간단히 갑시다 간단히
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

route = list(map(int, input().split()))
route_sum = [0] * (N+1)
sum = 0

for i in range(N):
    sum = sum + route[i]
    route_sum[i+1] = sum



if K > route_sum[N]:
    K = 2 * route_sum[N] - K - 1  # -1 매우 중요

# print('hi', route_sum, K)

if K == route_sum[N]:
        print(N)
elif K > 0:
    for i in range(N):
        if route_sum[i] <= K < route_sum[i+1]:
            print(i+1)
else:  # 거리 0, 골
    print(1)


'''
골 지점 안 넣은게 아마 이 문제 나름대로의 양심이겠지만 그런 배려는 걍 무시
'''
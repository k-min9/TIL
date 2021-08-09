'''
치킨집을 고르는 현명한 방법이 있을것이다.
근데 난 모르게씀. 견적부터 내보자.

최대 치킨집 경우 수 13C6 = 1716 (울프람 알파) >> 이부분 CPython이라 더 빠를 수 있음
최대 집 수 50 * 2 = 100

17만이면 껌이죠
'''
import sys
input = sys.stdin.readline
from itertools import combinations

def chicken_len(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

homes = []
chickens = []

N, M = map(int, input().split())

for i in range(N):
    # 좌표를 튜플로 때려박는다.
    for j, val in enumerate(list(map(int, input().split()))):
        if val == 1:
            homes.append((i,j))
        elif val == 2:
            chickens.append((i,j))

#print('h', homes)
#print('c', chickens)

# 각 배치당 최소거리의 집합
answer = 100 * 100 + 1
for chicken in combinations(chickens, M):
    # 도시의 치킨거리
    sums = 0
    # 집마다 탐방
    for home in homes:
        s = 100  # sum
        # 그 집의 치킨 거리
        for ch in chicken:
            s = min(s, chicken_len(home,ch))
        sums += s
    # 결론    
    #print('wh', sums, ':', chicken)
    answer = min(answer, sums)
    

print(answer)

'''
도시의 치킨거리를 잘못 이해해서 다 풀어놓고 answer 출력하는데 한참 걸림
'''
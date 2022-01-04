'''
무조건 N병은 마신다 = 길이가 N인 슬라이딩 윈도우
접근 :
1. 도수별로 정리한다.
2. 슬라이딩 윈도우

간 레벨을 간 총합으로 이해했다가 엄청 피본 문제.
이러면 슬라이딩 윈도우가 아니라, 
문제를 끝까지 똑바로 읽읍시다.
'''
# # 이진탐색을 만족도에 맞추고, 이때의 len을 비교해서 N보다 작으면 최초의 리스트에서 읽고 끝낸다.

# import sys
# input = sys.stdin.readline

# # N일 동안(슬라이딩 윈도우 크기), 필요 만족도, 맥주 종류
# N, M, K = map(int, input().split())
# beers = [list(map(int, input().split())) for _ in range(K)]
# # 만족도 오름차순
# beers = sorted(beers)

# lo = 0
# hi = 2**31

'''
>> 1차시도 : 타임 아웃
import sys
input = sys.stdin.readline

# N일 동안(슬라이딩 윈도우 크기), 필요 만족도, 맥주 종류
N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]
# 도수(내림차순)
beers = sorted(beers,key=lambda x: -x[1])
beers_drinkable = list()

# 무슨 일이 있어도 N병 먹겠다는 의지
for _ in range(N):
    beer = beers.pop()
    # 간 레벨 갱신
    costs = beer[1]
    beers_drinkable.append(beer)

# 술통이 빌 때 까지 or 만족할때까지 돌리자 돌리자
while beers:
    while beers and costs == beers[-1][1]:
        beers_drinkable.append(beers.pop())
    # 만족도(내림차순)
    beers_drinkable = sorted(beers_drinkable,key=lambda x: -x[0])
    scores = 0
    for i in range(N):
        scores += beers_drinkable[i][0]
        # 만족했으면 나가라
        if scores >= M:
            print(costs)
            break
    # 술통 비어있지 않으면 간레벨 갱신 하여 다시 챌린지
    if not beers:
        costs = beers[-1][1]

if scores<M:
    print(-1)      

'''

# >> 리벤지 타임 : 키워드는 선호도 관리
import sys
from heapq import heappop, heappush
input = sys.stdin.readline

# N일 동안(슬라이딩 윈도우 크기), 필요 만족도, 맥주 종류
N, M, K = map(int, input().split())
beers = [list(map(int, input().split())) for _ in range(K)]  # (선호도, 도수)
beers = sorted(beers, key=lambda x : (x[1], x[0]))  # 도수 낮은 수로 먹기 전략

heap = list()
cnt = 0  # 만족도
answer = 0
for beer in beers:
    cnt += beer[0]
    heappush(heap, beer[0])
    if len(heap) == N:
        if cnt >= M:
            answer = beer[1]  # 도수
            break
        else:
            cnt -= heappop(heap)
else:
    print(-1)
    exit()

print(answer)





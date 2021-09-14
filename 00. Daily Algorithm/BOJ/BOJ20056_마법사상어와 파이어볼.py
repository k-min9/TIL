'''
감상 : 상어 시리즈면 삼성임??
N^2 =2500, K = 1000 이면 파볼내 비교 완전탐색으로 돌려도 충분은 하다. 안할거지만
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

# 상수(y,x)
MOVES = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

# 격자 크기, 파이어볼 수, 이동횟수
N, M, K = map(int, input().split())

# r:행, c:열, m : 질량, s : 속도 , d : 방향 
fireballs = [list(map(int, input().split())) for _ in range(M)]

# K번 수행
for _ in range(K):
    # 이동
    fireball_dict = defaultdict(list)
    for r, c, m, s, d in fireballs:
        r = (r + s * MOVES[d][0]) % N
        c = (c + s * MOVES[d][1]) % N
        fireball_dict[(r,c)].append([m, s, d])

    # print(fireball_dict)
    fireballs = list()
    for key, value in fireball_dict.items():
        # print('k', key, value)
        # 충돌 없음
        n = len(value)
        if n == 1:
            fireballs.append([key[0], key[1], value[0][0], value[0][1], value[0][2]])
        else:
            nm = 0
            ns = 0
            nd = 0 # 0부터 시작할지 1부터 시작할지
            for val in value:
                nm += val[0]
                ns += val[1]
                nd += val[2]%2
            # 최종
            nm = nm //5
            ns = ns //n
            if nd == n or nd == 0:
                nd = 0
            else:
                nd = 1
            
            # 소멸 여부 및 나눠서 발사
            if nm != 0:
                for i in range(4):
                    fireballs.append([key[0], key[1], nm, ns, 2*i+nd])
answer = 0
for r, c, m, s, d in fireballs:
    answer += m
print(answer) 


'''
키워드는 딕셔너리에 튜플은 키로 쓸 수 있다. 대상들을 선언 없이 거의 객체 처럼 굴릴 수 있음
다 끝나고 찾아보니까 삼성거여서 defaultdict는 사용 못할지도 모르겠다.
근데 defaultdict 정도는 그냥 있는지 확인하고 넣는 정도의 차이여서 시험장에서도 이렇게 풀었을 듯
'''
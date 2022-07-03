'''
조건을 만족하는 문제의 가지수 구하기

콤비네이션도 될거 같고
문제 수 15개니까 그냥 그 문제 골랐네 안 골랐네로 비트마스킹도 가능할거 같고...
'''
import sys
input = sys.stdin.readline


# 문제 수, 문제난이도합최소,최대, 최고최저난이도차이
N, L, R, X = map(int, input().split())
difficulties = list(map(int, input().split()))

answer = 0
for i in range(1<<N):
    sums = 0  # 조건 : 합이 L과 R 사이
    cnt = 0  # 조건 : 두 문제 이상
    easy = 987654321  # 조건 : 차이가 X 이상
    hard = 0
    for j in range(N):
        if i & (1<<j):  # 골라짐
            sums += difficulties[j]
            cnt += 1
            easy = min(easy, difficulties[j])
            hard = max(hard, difficulties[j])
    
    if cnt >= 2 and hard-easy >= X and L <= sums <= R:
        answer += 1

print(answer)

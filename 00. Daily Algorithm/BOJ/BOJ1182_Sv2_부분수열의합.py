'''
속도나 효율성 제한도 없는데 이렇게 내면 그야 콤비네이션 쓰지 않을까?
'''
import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(1, N+1):
    comb = combinations(nums, i)

    for x in comb:
        if sum(x) == S:
            answer += 1

print(answer)

'''
그게 또 되버리구...
'''
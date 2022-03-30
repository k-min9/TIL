'''
끝자리수만 기록하는 DP면 될거같음
'''
import sys
input = sys.stdin.readline


# 상수
MOD = 10007


dp = [[1]*10]
N = int(input())

for i in range(N-1):
    now = dp[-1]
    next = [0]*10
    for j in range(10):
        for k in range(j+1):
            next[j] += now[k]
        next[j] %= MOD
    dp.append(next)

print(sum((dp[-1]))%MOD)

'''
MOD 안 써서 한번 틀리긴했는데 난이도 자체는 거의 브론즈 아닌가 이거...
난이도 기여 보니까 아닌가 보다.
'''
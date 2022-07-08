'''
브루탈...? 이걸?
'''
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
S = set(map(int, input().split()))

answer = sys.maxsize

for i in range(1, 1002):
    if i in S: continue
    for j in range(1, 1002):
        if j in S: continue
        for k in range(1, 1002):
            if k in S: continue
            target = abs(N - i*j*k)
            if target < answer:
                answer = target
            if target > N:
                break

print(answer)

'''
범위 설정때문에 엄청 애먹었음
'''
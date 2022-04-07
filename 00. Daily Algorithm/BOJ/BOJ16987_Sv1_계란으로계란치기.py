'''
요약 : 충돌시 상대의 무게만큼 내구도 각각 감소...
'''
import sys
input = sys.stdin.readline

N = int(input())
hp = [0] * N
weights = [0] * N

for i in range(N):
    hp[i], weights[i] = map(int, input().split())

res = 0 
def backtrack(idx, eggs):
    global res
    if idx == N:
        cnt = 0
        for i in range(N):
            if eggs[i] <= 0:
                cnt +=1
        if cnt > res:
            res = cnt
        return

    if eggs[idx] > 0:
        for i in range(N):
            flag = False
            # 충돌!
            if eggs[i] > 0 and i != idx:
                flag = True
                # 기존 리스트 복사
                tmp = eggs[:]
                tmp[i] -= weights[idx]
                tmp[idx] -= weights[i]
                backtrack(idx+1, tmp)
        if not flag:
            backtrack(idx+1, eggs)
    else:
        backtrack(idx+1, eggs)

backtrack(0, hp)
print(res)




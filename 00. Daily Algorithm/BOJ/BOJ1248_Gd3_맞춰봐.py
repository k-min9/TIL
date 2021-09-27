'''
접근 : 
1. 일단 표를 그린다.
2. 대각선에 있는것으로 부호를 알 수 있다. 21^10 > 10^10으로 계산 수 단축
3. 2초면 4천만, 지금은 100억...
'''
import sys
input = sys.stdin.readline

def backtrack(idx):
    if idx == N:
        return True 
    if graphs[idx][idx] == 0:  # answers[idx] = 0 > 패스
        return backtrack(idx + 1)
    for i in range(1,11):
        answers[idx] = graphs[idx][idx] * i
        if chk(idx) and backtrack(idx+1):
            return True
    return False

def chk(idx):
    sums = 0
    for i in range(idx, -1, -1):  # 역순으로 더하며 가지치기
        sums += answers[i]
        if sums == 0 and graphs[i][idx] != 0:
            return False
        if sums < 0 and graphs[i][idx] >= 0:
            return False
        if sums > 0 and graphs[i][idx] <= 0:
            return False
    return True

N = int(input())

cnt = 0
tmp = list(input().rstrip())
graphs = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if tmp[cnt] == '+':
            graphs[i][j] = 1
        elif tmp[cnt] == '-':
            graphs[i][j] = -1
        cnt += 1

answers = [0]*N
backtrack(0)
print(*answers)

'''
앞으로 백트래킹 문제는 dfs가 아니라 backtrack 이라는 함수로 등록하기로 했음.
'''
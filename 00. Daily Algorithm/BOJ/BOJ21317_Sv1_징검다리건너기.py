'''
일기장 : 공통 프로젝트 1등으로 끝날거 같은 분위기 + 내일은 토익!
견적 : 거꾸로 하는 DP도 재밌어보이고, 백트래킹도 될거 같고 뭐부터 해볼까아...
'''
import sys
input = sys.stdin.readline


def dfs(idx, can_bigjump, sums):
    if idx == N:
        global answer
        answer = min(answer, sums)
        return
    if idx > N:
        return
    # 매우 큰 점프
    if can_bigjump:
        dfs(idx+3, False, sums + energy_big)
    # 큰 점프
    dfs(idx+2, can_bigjump, sums + energies[idx][1])
    # 작은 점프
    dfs(idx+1, can_bigjump, sums + energies[idx][0])

# 돌의 개수
N = int(input())
energies = [0] + [list(map(int, input().split())) for _ in range(N-1)]  # x->x+1로 넘어갈때의 소모 에너지
energy_big = int(input())

answer = 987654321
dfs(1, True, 0)
print(answer)

'''
한번에 되어 버렸다;; 실버라 그런가 ㅠㅠ
'''
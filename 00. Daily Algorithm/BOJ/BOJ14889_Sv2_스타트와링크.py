'''
반으로 나눠서 하나하나 합하는 느낌인가...
차이가 안보이니 일단 브루탈 dfs
'''
import sys
input = sys.stdin.readline

def dfs(index):
    global answer
    if index == N//2:
        sum_team1 = 0
        sum_team2 = 0
        for i in range(0,N):
            if i not in team1:
                team2.append(i)  # team2는 그때 그때 계산후 비워주는 방식으로.
        for i in range(0, N//2 - 1):
            for j in range(i+1, N//2):
                sum_team1 += graphs[team1[i]][team1[j]] + graphs[team1[j]][team1[i]]
                sum_team2 += graphs[team2[i]][team2[j]] + graphs[team2[j]][team2[i]]
        diff = abs(sum_team2 - sum_team1)
        answer = min(answer, diff)
        team2.clear()
        return
    #dfs 시행
    for i in range(N):
        if i in team1: continue
        if len(team1)>0 and team1[len(team1)-1]> i : continue
        team1.append(i)
        dfs(index + 1)
        team1.pop()

# 입력
N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]

team1 = []
team2 = []
answer = float('Inf')
dfs(0)
print(answer)

'''
이게 되버려서 실버인가보다.
'''
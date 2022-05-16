'''
DFS로 브루트하게 밀면 될거같긴한데...
콤비네이션(조합)으로 팀 리스트 뽑아도 될 것 같음
'''
import sys
input = sys.stdin.readline

# 이번에 추가할 사람, 스타트팀, 링크 팀 현재 상황
def dfs(index, start, link) :
    if index == n :
        if len(start) == n or len(link) == n :
            return -1
            
        team_start = 0
        team_link = 0

        for i in range(len(start)) :
            for j in range(i+1, len(start)) :
                if i == j : 
                    continue
                team_start = team_start + s[start[i]][start[j]] + s[start[j]][start[i]]
        
        for i in range(len(link)) :
            for j in range(i+1, len(link)) :
                if i == j : 
                    continue
                team_link = team_link + s[link[i]][link[j]] + s[link[j]][link[i]]

        diff = abs(team_start - team_link)
        return diff
    
  

    if len(start) > n or len(link) > n : 
        return -1

    ans = -1

    # index의 사람을 start 팀에 넣었을 때
    team_start = dfs(index+1, start+[index], link)
    if ans == -1 or (team_start != -1 and ans > team_start) :
        ans = team_start

    # index의 사람을 link 팀에 넣었을 때
    team_link = dfs(index+1, start, link+[index])
    if ans == -1 or (team_link != -1 and ans > team_link) :
        ans = team_link

    return ans


# 입력
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

print(dfs(0,[],[]))

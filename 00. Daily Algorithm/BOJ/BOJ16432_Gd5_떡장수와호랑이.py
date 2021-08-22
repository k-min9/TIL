'''
루트를 기록하는 DFS
'''

import sys
input = sys.stdin.readline
# 내가 이거때문에 DFS가 꺼려지는데 얘는 이게 맞는거 같음
sys.setrecursionlimit(1000000) 

def dfs(prev, day):
    global flag
    # 도달!
    if day == N:
        flag = True
        return

    for i in range(1,len(cakes[day])):
        if flag == True:
            return
        cake = cakes[day][i]
        if cake != prev and not visited[day][i]:
            answers[day] = cake
            visited[day][i] = 1
            dfs(cake, day+1)


N = int(input())
cakes = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*10 for _ in range(N)]
flag = False
answers = [0]*N

# 0번째날만 존재하는 프로토타입 0번째 떡
dfs(0,0)
if flag:
    for answer in answers:
        print(answer)
else:
    print(-1)


'''
이론상으로 밖에 존재하지 않는 프로토타입의 시작품이라던가 로망입니다.
'''
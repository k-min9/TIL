'''
플로이드 와샬 후 거리가 2 이하인 노드의 갯수가 가장 많은 것
'''

import sys
input = sys.stdin.readline

# 상수
INF = 1e9

# 입력
N = int(input())
friends = [[INF]*N for _ in range(N)]
for y in range(N):
    friend = input().rstrip()
    for x in range(N):
        if friend[x] == 'Y':
            friends[y][x] = 1

for i in range(N):
    friends[i][i] = 0

# 플로이드
for k in range(N):
    for i in range(N):
        for j in range(N):
            if friends[i][j] > friends[i][k] + friends[k][j]:
                friends[i][j] = friends[i][k] + friends[k][j]

# 결과
answer = 0
for friend in friends:
    cnt = -1  # 본인 제외
    for f in friend:
        if f <= 2:
            cnt += 1
    answer = max(answer, cnt)

print(answer)

'''
조금 과하게 풀긴 했는데 플로이드 연습겸...
3-친구였으면 골드 문제였을 듯
'''
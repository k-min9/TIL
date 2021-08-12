import sys
input = sys.stdin.readline

INF = 1e9
N = int(input())

# 인풋
maps = [[INF]*26 for _ in range(26)]

for _ in range(N):
    a, trash, b = input().split()
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    maps[a][b] = 1

# 'a is a'
for i in range(26):
    maps[i][i] = 0

# for m in maps:
#     print(*m)

# 플로이드
for k in range(26):
    for i in range(26):
        for j in range(26):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]

# 'a is a'
for i in range(26):
    maps[i][i]=1

for m in maps:
    print(*m)

# 출력
M = int(input())
for _ in range(M):
        a, trash, b = input().split()
        a = ord(a) - ord('a')
        b = ord(b) - ord('a')
        
        # 가는 길 없음
        if maps[a][b] == 0 or maps[a][b] == INF:
            print('F')
        else:
            print('T')
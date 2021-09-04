'''
m도 없고 어디서 문제 만들다가 말거나 다른 문제 잘라서 만든 문제 같은데
'''
import sys
input = sys.stdin.readline

# 테두리 상수
bounds = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 이름 뭐라고 지어야 될 지도 모르겠다. 숫자 새기기
def marking(y, x):
    for dy, dx in bounds:
        ny = y + dy
        nx = x + dx
        if 0<=ny<N and 0<=nx<N:
            graphs_num[ny][nx] += 1 

# 격자 크기 및 정보
N = int(input())
graphs = [input().rstrip() for _ in range(N)]
graphs_num = [[0]*N for _ in range(N)]

# 지뢰 별도 보관
traps = list()

for y in range(N):
    for x in range(N):
        if graphs[y][x] == '*':
            traps.append((y, x))
            marking(y, x)

# for g in graphs_num:
#     print(*g)

# 지뢰 밟음 여부
flag = False
for y in range(N):
    words = input().rstrip()
    for x in range(N):
        if words[x] == '.':
            # 저는 이게 파이썬의 강점이라고 봅니다.
            graphs_num[y][x] = '.'
        elif graphs[y][x] == '*':
            # 지뢰 밟음
            flag = True

print(traps)
if flag:
    for y, x in traps:
        graphs_num[y][x] = '*'

for g in graphs_num:
    print(''.join(map(str,g)))
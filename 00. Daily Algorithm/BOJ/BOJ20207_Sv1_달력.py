'''
구현이지 뭐
'''
import sys
input = sys.stdin.readline

N = int(input())

calender = [[0] * 366 for _ in range(N)]

todo = list()

for _ in range(N):
    s, e = map(int, input().split(' '))
    term = e - s + 1
    todo.append((s, e, term))

todo.sort(key=lambda x: (x[0], -x[2]))

for k in range(len(todo)):
    s, e = todo[k][0], todo[k][1]

    for i in range(N):
        if 1 in calender[i][s:e + 1]:
            continue

        for j in range(s, e + 1):
            calender[i][j] = 1
        break

row = 0
col = 0
ans = 0
for j in range(1, 366):
    one_check = False
    for i in range(N):
        if calender[i][j] == 1:
            one_check = True
            row = max(row, i + 1)
    if one_check:
        col += 1
    else:
        ans += row * col
        row = 0
        col = 0
if one_check:
    ans += row * col

print(ans)

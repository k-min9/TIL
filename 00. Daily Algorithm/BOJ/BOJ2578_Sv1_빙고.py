'''
요즘 실버 구현 많은데 손 풀이로 좋은거 같음
5 5 사이즈면 무슨 깽판을 쳐도 된다는 확신이 있음
'''
import sys
input = sys.stdin.readline

graphs = [list(map(int, input().split())) for _ in range(5)]
bingos_list = list()

querys = [list(map(int, input().split())) for _ in range(5)]
querys_list = list()
for query in querys:
    querys_list.extend(query)

for x in range(5):
    tmp = set()
    for y in range(5):
        tmp.add(graphs[y][x])
    bingos_list.append(tmp)

for y in range(5):
    tmp = set()
    for x in range(5):
        tmp.add(graphs[y][x])
    bingos_list.append(tmp)

tmp = set()
for i in range(5):
    tmp.add(graphs[i][i])
bingos_list.append(tmp)

tmp = set()
for i in range(5):
    tmp.add(graphs[i][4-i])
bingos_list.append(tmp)


for answer in range(25):
    query = querys_list[answer]
    cnt = 0
    for bingo in bingos_list:
        if query in bingo:
            bingo.remove(query)
        if len(bingo) == 0:
            cnt += 1
    if cnt >= 3:
        break

print(answer + 1)

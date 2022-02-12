'''
5*7 사이즈의 그림 N개 완전탐색?
'''
import sys
input = sys.stdin.readline


# 그림 갯수
N = int(input())
pictures = list()
for _ in range(N):
    pictures.append([input().strip() for _ in range(5)])

answer1, answer2 = 0, 0
mincnt = 987654321
for i in range(N):
    for j in range(i+1, N):
        cnt = 0
        for y in range(5):
            for x in range(7):
                if pictures[i][y][x] != pictures[j][y][x]:
                    cnt += 1

        # 답은 하나 (대전제)
        if cnt < mincnt:
            mincnt = cnt
            answer1 = i
            answer2 = j

print(answer1+1, answer2+1)

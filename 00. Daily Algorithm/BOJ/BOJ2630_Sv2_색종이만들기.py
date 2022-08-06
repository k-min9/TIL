'''
~분할정복 Festival~ 1/10
'''
import sys
input = sys.stdin.readline


def divide_paper(num, paper):
    global count_white, count_blue

    # 색종이 제작 여부
    chk = 0
    for i in range(num):
        chk += sum(paper[i])
    if chk == 0:  # 흰색종이
        count_white += 1
    elif chk == num*num:  # 파란 종이
         count_blue += 1
    else:  # 추가 분할 필요
        temp = [paper[i][0:num//2] for i in range(0,num//2)]  # 4개로 나눠서 위 과정을 반복
        divide_paper(num//2,temp)
        temp = [paper[i][0:num//2] for i in range(num//2,num)]
        divide_paper(num//2,temp)
        temp = [paper[i][num//2:num] for i in range(0,num//2)]
        divide_paper(num//2,temp)
        temp = [paper[i][num//2:num] for i in range(num//2,num)]
        divide_paper(num//2,temp)


N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

count_white = 0
count_blue = 0

divide_paper(N, papers)
print(count_white)
print(count_blue)

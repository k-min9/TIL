'''
접근 : 체크함수 만들고 싹 돌리기? 
아니 2500자리 체스판에 2초나 주는건 막 풀라는거 아님???
'''

import sys
input = sys.stdin.readline


#1. 8*8 체크 함수
def checkChess(idxRow, idxCol):
    answer = 0
    for i in range(8):
        if i%2: #홀수번 W 아닐때 B (역순이어도 상관 없음)
            nextBoard = 'B'
        else:
            nextBoard = 'W'
        for j in range(8):
            if chessBoards[idxRow+i][idxCol+j] != nextBoard:
                answer = answer + 1
            if nextBoard == 'B':
                nextBoard = 'W'
            else:
                nextBoard = 'B'

    return min(answer, 64-answer)

# 입력
N, M = map(int, input().split())

chessBoards = [] #체스판 리스트
for i in range(N):
    chessBoards.append(input().rstrip())

result = M*N+1
for i in range(M-7):
    for j in range(N-7):
        result = min(result, checkChess(j,i))
        #print('result', i, j, result)
print(result)

'''
행과 열 거꾸로 입력했다가 한번 틀린 사람 나말고도 있을거라고 믿습니다. ㄹㅇ루...
'''
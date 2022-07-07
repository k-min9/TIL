'''
나름의 법칙으로 찍어서 10개중에 5개를 맞출 경우의 수???
combination으로 5지선다 10개를 돌리면 터질테고 흐음...
dp?
'''
import sys
input = sys.stdin.readline

def backtrack(depth):
    global answer
    # 선택 완료
    if depth == 10:
        s = 0
        for j in range(10):
            if selects[j] == answers[j]:
                s += 1
        if s >= 5:
            answer += 1
        return

    # 법칙
    for i in range(1, 6):  # 5지선다
        if depth > 1 and selects[depth-2] == selects[depth-1] == i:
            continue
        selects.append(i)
        backtrack(depth+1)
        selects.pop()
        
# 정답 리스트, 선택 리스트, 정답
answers = list(map(int, input().split()))
selects = list()
answer = 0
backtrack(0)
print(answer)

'''
접근 : 백트래킹 문제랜다. 체스판에 퀸을 끼워넣고 싶다.
파이썬은 백트래킹 어떻게 하나 봤더니 다들 global 쓴다.
저어는 그런거 좀 안좋아하는데;;

애초에 마지막 순간까지 가지치기를 못하는데 왜 백트래킹을 씀???
그래서 한 번 해 봄
'''
import sys
input = sys.stdin.readline

def backTrackDFS(idx, result):

    global ansMin
    global ansMax

    if idx == n-1:
        ansMin = min(ansMin, result)
        ansMax = max(ansMax, result)
        return result
    
    for i in range(4):
        temp = result
        if opers[i] == 0:
            continue
        if i == 0:
            result = result + numbers[idx+1]
        elif i == 1:
            result = result - numbers[idx+1]
        elif i == 2:
            result = result * numbers[idx+1]
        else:
            if result < 0:
                result = -(abs(result) // numbers[idx+1])
            else:
                result = result // numbers[idx+1]
        opers[i] = opers[i] - 1
        backTrackDFS(idx+1,result)
        opers[i] = opers[i] + 1
        result = temp


#Min, Max
ansMin = 1000000001
ansMax = -1000000001 

#실행
n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

backTrackDFS(0, numbers[0])

print(ansMax)
print(ansMin)

'''
개선 여지도 있어보이지만,
진짜 전부 순회함.
가지치기 없는 백트래킹???
뭐가 하고 싶었던거지?
모르겠다. 머리가 안 돌아간다.
'''
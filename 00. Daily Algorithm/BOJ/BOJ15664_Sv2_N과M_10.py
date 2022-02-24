'''
N과 M 시리즈 오랜만
N, M : 1~8 , 10000이하의 수
itertools 봉인해보고 오랜만에 백트래킹!
'''
import sys
input = sys.stdin.readline


def backtrack(answer, idx, cnt):
    global M
    if cnt == M:
        if answer not in answers:
            answers.append(answer)
            print(*answer)
        return

    if idx >= N:
        return
    
    for next in range(N-idx):
        backtrack(answer + [nums[idx+next]], idx + next + 1, cnt + 1)



N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answers = list()

backtrack([], 0, 0)





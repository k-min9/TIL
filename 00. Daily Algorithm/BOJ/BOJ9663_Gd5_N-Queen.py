'''
대표적인 백트래킹 문제
'''

import sys
input = sys.stdin.readline

# queen이 존재하는 column
# col에 대해 모든 row에 검사(여기서 백트래킹 발생)
def backtrack(queen, row):
    count = 0
    if row == N:
        return 1
    for col in range(N):
        queen[row] = col
        for i in range(row):
            # 여기에서 백트래킹 발생
            if queen[i] == queen[row]:
                break
            # 여기에서 백트래킹 발생
            if abs(queen[i] - queen[row]) == row - i:
                break
        else:
            count = count + backtrack(queen, row+1)
    return count

N = int(input())
print(backtrack([0]*N, 0))

'''
N이 15이하인데 주어진 시간이 10초다.
>>N이 작을때만 사용할 수 있음!
'''

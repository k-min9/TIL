'''
N이 5000 = 하고 싶은데로 하세요
'''
import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))
answer = 3000000001
answers = [liquids[0], liquids[1], liquids[-1]]
for i in range(n-2):

    left = i + 1
    right = n - 1
    #절대값 작아지면 갱신, 음수면 왼쪽에서 인덱스 전진 양수면 우측에서 인덱스 전진
    while left < right:
        tmp = liquids[i] + liquids[left] + liquids[right]
        # 절대값 작아지면 갱신
        if abs(answer) > abs(tmp):
            answer = tmp
            answers = [liquids[i], liquids[left], liquids[right]]
        # 음수면 왼쪽에서 인덱스 전진, 양수면 우측에서 인덱스 전진
        if tmp < 0:
            left = left + 1
        else:
            right = right - 1

print(*answers)       

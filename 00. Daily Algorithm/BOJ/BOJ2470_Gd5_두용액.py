'''
N=10만 견적 O(NlogN) 
대놓고 소트 후 -> 투 포인터
'''
import sys
input = sys.stdin.readline

n = int(input())
liquids = sorted(list(map(int, input().split())))

left = 0
right = n - 1
answer = liquids[left] + liquids[right]
answers = [liquids[left], liquids[right]]
#절대값 작아지면 갱신, 음수면 왼쪽에서 인덱스 전진 양수면 우측에서 인덱스 전진
while left < right:
    tmp = liquids[left] + liquids[right]
    # 절대값 작아지면 갱신
    if abs(answer) > abs(tmp):
        answer = tmp
        answers = [liquids[left], liquids[right]]
    # 음수면 왼쪽에서 인덱스 전진, 양수면 우측에서 인덱스 전진
    if tmp < 0:
        left = left + 1
    else:
        right = right - 1

print(*answers)       
'''
먼가... 먼가 생활감이 묻어나오는 문제
견적 백만? 완전 탐색 고고
'''
import sys
input = sys.stdin.readline

# 입력
target = int(input())
# 정답이 될 수 있는 최대값
answer = abs(100 - target)
# 고장난 버튼 수
M = int(input())
if M:
    broken = set(input().split())
else:
    broken = set()

# 큰 수에서 작은 수로 가니까 탐색 숫자 : 백만번 * N
for num in range(1000001): 
    for N in str(num):
    # 번호를 눌러서 만들 수 없는 경우엔 스탑
        if N in broken: 
            break
    # 번호를 눌러서 만들 수 있는 경우엔 min(최대값, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
    else: 
        answer = min(answer, len(str(num)) + abs(num - target))

print(answer)
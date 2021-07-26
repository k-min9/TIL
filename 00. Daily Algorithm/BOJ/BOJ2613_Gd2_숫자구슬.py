'''
접근 : 한석봉 떡 썰기도 아니고, 구슬 썰기다.
어쨌든 파라메트릭 문제라는거
'''
# 기본 전처리
import sys
input = sys.stdin.readline

# 현재 총합을 넘지 않는 그룹이 총 몇 그룹
def getBallGroup(mid):
    gNum = 1  # 반환용 그룹 수
    gSum = mid  # 총합 체크
    gList = [0] # 그룹 소속 인원 체크
    for ball in balls:
        if gSum >= ball:
            gSum = gSum - ball
            gList[-1] = gList[-1] + 1
        elif mid < ball:  # mid 자체를 올리기 위해 우측이동 필요
            gNum = (N * 100)  # MAX
        else:
            gNum = gNum + 1
            gSum = mid - ball
            gList.append(1)
    return gNum, gList

# 구슬 개수, 그룹 수, 구슬 숫자
N, M = map(int, input().split())
balls = list(map(int, input().split()))

# 이진 탐색 기준 : 최대 SUM
lo = 0
hi = N * 100

# 이진 탐색 시작
while(lo < hi):
    mid = (lo+hi) // 2
    if M >= getBallGroup(mid)[0]:  # 그룹 수 적음 = 좌측 이동
        hi = mid
    else: #  그룹 수 많음 = 우측 이동
        lo = mid + 1
    #print('bisect', lo, mid, hi, getBallGroup(mid))
    mid = lo

answers = getBallGroup(mid)[1]  # 여분의 연산
if len(answers) != M:
    while(len(answers) < M):
        for i in range(len(answers)):
            if answers[i] > 1:
                answers[i] = answers[i] - 1
                answers.insert(i,1)
                if len(answers) == M:
                    break

print(mid)
print(*answers)


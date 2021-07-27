'''
접근 : 인접한 원소들로 구성이면 이거 개꿀아닌가요
키워드 : 애드혹, 투 포인터

애드혹이 뭐야??? >> 비정규적 직관
'''

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.append(0)  # 인덱스 에러 방지

#투포인터 현명하게 전진 버전 ~실질적으로 O(N)
pointL = 0
pointR = 0 # 첫 R만 0에서 시작해야 2 / 2 2 잡아냄??
answer = 1

for i in range(N):
    while(pointR<N):
        #print('go', pointL, pointR)
        if nums[pointR] < nums[pointR+1]:
            pointR = pointR + 1
        elif nums[pointR] == nums[pointR+1]:  # 짝수 pel 점검
            length = 0
            for j in range(pointR-pointL+1):
                if nums[pointR-j] == nums[pointR+1+j]:
                    length = length + 2
                else:
                    break
            answer = max(answer, length)
            pointL = pointL + length - 1
            pointR = pointL
        else:  # 홀수 pel 점검
            length = -1
            for j in range(pointR-pointL+1):
                # print('go', nums[pointR-j], nums[pointR+j])
                if nums[pointR-j] == nums[pointR+j]:
                    length = length + 2
                else:
                    break
            answer = max(answer, length)
            pointL = pointL + length
            pointR = pointL
        # print('l', pointL)

print(answer)         

'''
#투포인터 무식하게 전진 버전 >>> 시간 초과

def isPelA(pointL, pointR): # 짝수 pel
    i = pointR-pointL
    for j in range(1,i):
        if nums[pointR-j-1] != nums[pointR+j]:
            return False
    return True

def isPelB(pointL, pointR): # 홀수 pel
    i = pointR-pointL
    for j in range(1,i):
        #print('C', pointR, nums[pointR-1-j], nums[pointR-1+j])
        if nums[pointR-1-j] != nums[pointR-1+j]:
            return False
    return True


pointL = 0
pointR = 1
answer = 1

for i in range(N):
    while(pointL<N-1):
        #print('p', pointL)
        if nums[pointR-1] < nums[pointR]:
            pointR = pointR + 1
            if pointR == N:
                pointL = pointL + 1
                pointR = pointL + 1
        elif nums[pointR-1] == nums[pointR]:
            #짝수 pel인지 확인
            #print('A', nums[pointL:pointR], nums[pointR*2-pointL-1:pointR-1:-1])
            if isPelA(pointL, pointR): # 빙고
                answer = max(answer, 2*(pointR-pointL))
                pointL = pointR
                pointR = pointL + 1
            else:
                pointL = pointL + 1
                pointR = pointL + 1
        else:
            #홀수 pel인지 확인
            #print('B', nums[pointL:pointR-1], nums[pointR*2-pointL-2:pointR-1:-1])
            if isPelB(pointL, pointR): # 빙고
                answer = max(answer, 2*(pointR-pointL)-1)
                pointL = pointR
                pointR = pointL + 1
            else:
                pointL = pointL + 1
                pointR = pointL + 1
'''



'''
감상 : 반나눠서 전부 더하고, 최대치 꺾이면, 멈추고 갱신하고... 맞나?
키워드 : '투 포인터'
접근 : 
찾아보니 이쪽이 빠른 알고리즘이다. 
뭔가 이런거 배웠던 기억이 있는거 같기도 하고...
'''
import sys

n = int(input())
liquids = list(map(int, sys.stdin.readline().rstrip().split())) #stdin.readline은 좀 더 써봐야 익숙해질 듯

#이것이 투포인터다!
leftIdx = 0
rightIdx = n - 1
answer = liquids[leftIdx] + liquids[rightIdx]

#절대값 작아지면 갱신, 음수면 왼쪽에서 인덱스 전진 양수면 우측에서 인덱스 전진
while leftIdx < rightIdx:
    tmp = liquids[leftIdx] + liquids[rightIdx]
    # 절대값 작아지면 갱신
    if abs(answer) > abs(tmp):
        answer = tmp
    # 음수면 왼쪽에서 인덱스 전진, 양수면 우측에서 인덱스 전진
    if tmp < 0:
        leftIdx = leftIdx + 1
    else:
        rightIdx = rightIdx - 1

print(answer)       

'''
감상 : 무식한짓하지 말라고 배우는게 알고리즘이라는걸 다시 한 번 느꼈습니다!
'''
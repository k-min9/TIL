'''
감상 : 트위치 포켓몬 챌린지라고 들어본적 있으세요?
접근 : 
1. D의 갯수가 배열 숫자보다 크면 바로 에러
2. 수행함수 10만, 배열 구성원 100이하면 순서대로 해도 1초 연산(2천만) 될거같은데
3. 뒤집기를 실제로 뒤집으면 안된다. 이거하는 순간 타임 아웃.(아마 이거 묻는 문제)
'''

import sys
import ast #문자열 모양 리스트를 리스트로 변환하는 모듈

input = sys.stdin.readline

n = int(input())

for _ in range(n):

    # 정보 정리
    command = input()
    length = int(input())
    arr = input() #현재 리스트 모양의 문자열

    if length < command.count('D'):
        print('error')
        continue
    
    arr = ast.literal_eval(arr) #모듈 만세

    # 작업 전 초기화

    LeftIdx = 0 #왼쪽
    RightIdx = length #오른쪽
    reverseFlag = False #현재 뒤집힌 상태인지

    
    for i in range(len(command)-1):
        if command[i] == 'R':
            reverseFlag = not reverseFlag
        else:
            if reverseFlag:
                RightIdx = RightIdx - 1
            else:
                LeftIdx = LeftIdx + 1                
    
    arr = arr[LeftIdx:RightIdx]

    #최종 뒤집기
    if command.count('R')%2: #1 = 뒤집어라
        arr = arr[::-1]    

    #list to str
    print(str(arr).replace(' ', ''))
    
    
'''
아까의 join과 replace가 뻘짓이 아니었다. 입력 출력 포맷 맞추는게 제일 힘듬
자료구조  안 쓴 이유 : 2천만번 계산이 진짜 1초만에 가능한지 궁금 >> 진짜로 빡빡했지만 통과
연산 횟수 대충 생각해보고, 이 방법이 먹힐지 계산하는 것이 중요하다고 느낌
'''
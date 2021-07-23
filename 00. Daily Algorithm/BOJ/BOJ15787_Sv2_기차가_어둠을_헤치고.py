'''
감상 : 
와! 2진수! 
와! 비트연산! 
해서 C처럼 풀어도 좋지만 성실하게 하기로 했습니다.
와! 중복체크! 끝! << 이걸로 그렇게 고생할 줄 몰랐지
'''

import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 기차 수, 명령 수

trains = [[0]*20 for _ in range(N)] #기차정보 2차원 리스트

#명령 실행
for _ in range(M):
    order = list(map(int, input().rstrip().split()))

    #동무들 지령이오
    if order[0] == 1: #앉으시오
        trains[order[1]-1][order[2]-1] = 1
    elif order[0] == 2: #일어나시오
        trains[order[1]-1][order[2]-1] = 0
    elif order[0] == 3: #우로 한칸 가시오
        trains[order[1]-1].pop() #우측은 시베리아행
        trains[order[1]-1].insert(0,0) #한개면 인서트 써도 됨!
    else: #좌로 한칸 가시오 #메ㅡ우 위험한 행동
        trains[order[1]-1] = trains[order[1]-1][1:]#좌측은 시베리아행
        trains[order[1]-1].append(0)#우측에 빈자리 생김

#중복제거
answer = set()
for train in trains:
    answer.add(''.join(map(str,train)))
print(len(answer))


'''
감상 : 아니 명령 내리라길래...

배운것
1. 다음에는 command = order[0], trainNum = order[1]-1, seatNum=order[2]-1로 나눈다 진짜로
2. 2차원 리스트를 set로 중복 체크하고 싶으면 중간에 튜플을 끼면 된다고 한다. 
set(list(map(tuple, trains)))면 끝
내 시간... 내 노력...
그래도 join 함수 사용법 익혔으니까 만족하는 걸로 하자.
'''
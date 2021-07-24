'''
접근 : 
1. 시작시간 빠른 순으로 소트를 하고,
2. 회의 정보 담을 리스트를 만든다. 담는 내용은 최후시간 하나.
3. 리스트와 내용 비교해서, 자신이 모든 내용물보다 크면, 새로운 칸을 만든다.
4. 리스트의 길이를 출력한다.
<<<실패

3차접근 :
키워드 : 우선순위 큐 << 끝나는 시간에 최소heap 하라는 소리다.
'''
#전처리
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

#총 회의 수
N = int(input())

#리스트의 형태로 회의 정보 받기
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))
meetings.sort() #찾아보니 2차리스트 첫값으로 sort 할때는 meetings.sort(key=lambda x:x[0]) 필요 없음

#끝나는 시간 최소 heap 관리하여 갱신
count = 0
endTimeHeap = []
for startTime, endTime in meetings:
    if endTimeHeap: #첫트라이 or 애초에 회의가 없음
        if endTimeHeap[0]<=startTime:
            heappop(endTimeHeap)
        heappush(endTimeHeap,endTime)
    else:
        heappush(endTimeHeap,endTime) #회의 갱신

print(len(endTimeHeap))





'''
<1차, 2차 시도 실패 기록>
#리스트 정렬하기
meetings.sort(key=lambda x:x[0])#, reverse=True) 
#두번째 값 비교 필요 없음, 역순으로 해야 pop 할때 원하는 순서대로 나옴

#접근 3 실행

#1차 시도 실패 << 시간 초과
# answers = [0]
# while(meetings): #뭔가 영단어 같을때 기분 좋음. is visited라던가
#     meeting = meetings.pop() #[0] : 시작시간, [1] : 종료시간
#     flag = False #갱신 여부

#     for i in range(len(answers)):
#         if answers[i] <= meeting[0]:
#             answers[i] = meeting[1]
#             flag = True
#             break

#     if not flag:# 회의 추가
#         answers.append(meeting[1])

# 2차 시도 실패 << 여전히 시간 초과. pop 안쓴만큼만 빨라짐. 의미 없었음.
# answers = [0]
# for meeting in meetings: #[0] : 시작시간, [1] : 종료시간
#     flag = False #갱신 여부

#     for i in range(len(answers)):
#         if answers[i] <= meeting[0]:
#             answers[i] = meeting[1]
#             flag = True
#             break

#     if not flag:# 회의 추가
#         answers.append(meeting[1])   
#         #count = count+1

# print(len(answers))       
'''
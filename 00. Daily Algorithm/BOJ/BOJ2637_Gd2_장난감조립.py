'''
감상 : 카탄 땡기네...
접근 : 중간부품끼리 간섭이 없으면 이거 걍 그리드로 밀면 되지 않나
키워드 : 그래프 이론, 위상 정렬 
네 시키는대로 합시다.
'''
import sys

#입력
n = int(input())
m = int(input())

#그래프 정보 입력용 리스트
graph = [[] for _ in range(n + 1)]
#위상정렬 진입차수(degree)
degree = [0] * (n + 1)

for _ in range(m):
    assemble, material, needed = map(int, sys.stdin.readline().split())
    graph[assemble].append([material, needed]) #방향성 있음
    degree[material] = degree[material] + 1 #이 재료를 요구할때 마다 추가

#내려가면서 기록
answer = [0] * (n + 1)
#완제품 번호 고정
answer[n] = 1

'''
1차 시도(그리드) <<<실패
#기본제품 수
basic = 0
for i in range(n):
    if bool(graph[i]) == False:
        basic = i


for i in range(n,basic,-1): #n~basic+1까지 그냥 쭉
    while answer[i] and bool(graph[i]): #n~1까지 쭉 쓴 댓가(비합리적))
        for j in graph[i]: #graph[7]에는 7에 필요한 부품 종류와 필요 갯수가 등록 되어있다.
            answer[j[0]] = answer[j[0]] + j[1]
        answer[i] = answer[i] - 1

#기본제품 커팅식
answer = answer[1:basic+1]

#출력
for i in range(basic):
    print(f'{i+1} {answer[i]}')
'''


while(sum(degree)): #진입차수가 0이 될때까지 루프
    
    for i in range(1, n+1):
        if degree[i] == 0 and bool(graph[i]): #진입할 차례 + 그래프가 비어있지 않음
            for j in graph[i]: #graph[7]에는 7에 필요한 부품 종류와 필요 갯수가 등록 되어있다.
                answer[j[0]] = answer[j[0]] + (j[1] * answer[i])
                degree[j[0]] = degree[j[0]] - 1 #진입차수 정리(i에 필요한 재료들 화살표 지우기)
            answer[i] = 0
            graph[i] = [] # 다 썼으면 그래프 비워버리고.

for i in range(len(answer)):
    if answer[i] !=0:
        print(f'{i} {answer[i]}')


'''
1차 감상 :
그리드 틀렸다. 이거 섞었네. 전면적으로 수정해야함.
'''

'''
2차 감상:
일단 지르고 느리면 자료구조 얹어야지 했는데, 생각 이상으로 빨랐다. 
그리드때보다 코드 더 짧은게 더 유머
그럼 여기서 일단 끝
'''
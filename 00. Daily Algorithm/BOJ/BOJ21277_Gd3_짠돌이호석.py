'''
감상 : 골드급 구현문제 ㄷㄷㄷㄷㄷㄷ
견적 : 
액자 최대크기 2500 
액자 돌리기 3번 = 10000회 연산
액자 합치기 4번 = 10000회 연산
    합칠때마다 체크 최대 50*50 = 2500회 연산
에엥????
접근 : 그래도 충돌하면 빠르게 break 할수도 있고 일단 박고 보자
'''

import sys
input = sys.stdin.readline

# 시계 방향 90도 회전 (파이써닉)
def rotate(graph):
    graph = list(zip(*graph))
    for i in range(len(graph)):
        graph[i] = graph[i][::-1]

    return graph

def chk1(x, y):
    # 그래프 1을 고정, 2를 이동
    # 이동축
    for p in range(N2):
        for q in range(M2):
            try:
                if 0<=y+p<N1 and 0<=x+q<M1 and graph1[y+p][x+q] == graph2[p][q] == '1':
                    return 5000
            except:
                print('what')
                pass
    # print('a',(max(N1,y+N2)-min(y,0)),(max(M1,x+M2)-min(x,0)),(max(N1,y+N2)-min(y,0))*(max(M1,x+M2)-min(x,0)))
    return (max(N1,y+N2)-min(y,0))*(max(M1,x+M2)-min(x,0))

# def chk2(x, y):
#     # 그래프 2를 고정, 1을 이동
#     # 이동축
#     for p in range(N2):
#         for q in range(M2):
#             try:
#                 if graph2[y+p][x+q] == graph1[p][q] == '1':
#                     return 5000
#             except:
#                 pass
#     return max(N2,y+N1)*max(M2,x+M1)


# 행, 열
N1, M1 = map(int, input().split())
graph1 = []

# 문자열 채로 넣어도 2차원 배열
for i in range(N1):
    graph1.extend(input().split())

# 행, 열
N2, M2 = map(int, input().split())
graph2 = []

# 문자열 채로 넣어도 2차원 배열
for i in range(N2):
    graph2.extend(input().split())

# 체크합시다.
answer = 5000  # 단하나도 안 맞아서 나란히 배치

# for _ in range(4):
#     graph1 = rotate(graph1)
#     N1, M1 = M1, N1
for _ in range(4):
    graph2 = rotate(graph2)
    N2, M2 = M2, N2

    for i in range(-N2, N1+1):
        for j in range(-M2, M1+1):
            answer = min(answer, chk1(j,i))


        # for i in range(N2):
        #     for j in range(M2):
        #         answer = min(answer, chk2(j,i)) 

print(answer)

'''
과정1. > 10개 맞음
스터디에 나온 파이써닉한 풀이가 도중에 있었음!!!
ㄴ이때까지만 해도 기분이 엄청 좋았음
과정2. > 14개 맞음
한쪽만 4번 돌리면 될 줄 알았는데 아니었음 
둘 다 4번씩 4*4번 돌려야 함
과정3. > 16개 맞음
1만 고정하는게 아니라 2도 고정해보자
과정4. > 정답
원점 회귀. 1을 고정하되 마이너스 범위를 줘서 체크하자

저어는 이 문제에 4시간이 걸릴줄 몰랐어요.
'''
'''
구현 
1. 종이와 펜을 들어라
2. 니가 조립하지 말고 컴퓨터를 시켜라
'''

import sys
input = sys.stdin.readline

# 입력(나중에 내려라)

N, R = map(int, input().split())
N = 2**N
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))

# 상하 반전
def rotate1(sx, sy, l):
    # 세로
    for i in range(l//2):
        # 가로
        for j in range(l):
            graph[i+sx][j+sy], graph[l-i-1+sx][j+sy] = graph[l-i-1+sx][j+sy], graph[i+sx][j+sy]

# 좌우 반전
def rotate2(sx, sy, l):
        for i in range(l):
            for j in range(l//2):
                graph[i+sx][j+sy], graph[i+sx][l-j-1+sy] = graph[i+sx][l-j-1+sy], graph[i+sx][j+sy]

# 오른쪽(시계) 90도 회전
def rotate3(sx, sy, l):
    # 그 부분을 잘라서
    tmp = [[0 for _ in range(l)] for _ in range(l)]
    # 돌려서
    for i in range(l):
        for j in range(l): tmp[i][j] = graph[l-j-1+sx][i+sy]   
    # 담는다
    for i in range(l):
        for j in range(l): graph[i+sx][j+sy] = tmp[i][j]

# 좌측(반시계) 90도 회전
def rotate4(sx, sy, l):
    # 그 부분을 잘라서
    tmp = [[0 for _ in range(l)] for _ in range(l)]
    # 돌려서
    for i in range(l):
        for j in range(l): tmp[i][j] = graph[j+sx][l-i-1+sy]
    # 담는다.
    for i in range(l):
        for j in range(l): graph[i+sx][j+sy] = tmp[i][j]

# 새로운 걸 도입하려면 중앙 제어가 필요해짐
def rotate(k, l):
    if k == 1:
        # 나는 정사각형 이럴때 좋음
        for i in range(N//l):
            for j in range(N//l): 
                rotate1(l*i, l*j, l)
    elif k == 2:
        for i in range(N//l):
            for j in range(N//l): 
                rotate2(l*i, l*j, l)
    elif k == 3:
        for i in range(N//l):
            for j in range(N//l): 
                rotate3(l*i, l*j, l)
    elif k == 4:
        for i in range(N//l):
            for j in range(N//l): 
                rotate4(l*i, l*j, l)  

# 솨ㅡ 모았다가.
def graph_group(l):
    # 손으로 써보면 복사도 필요 없고 연산 횟수 반으로 줄일 수 있음. 근데 구현을 못하겠다.
    tmp = [[0]*N for _ in range(N)]
    # N^4로 보이지만 N^2입니다. 아마.
    # 부분 배열 박스 그룹 개수
    for i in range(l):
        for j in range(l): 
            # 박스 내 수치
            for p in range(N//l):
                for q in range(N//l):
                    tmp[(N//l)*i+p][(N//l)*j+q] = graph[i+p*l][j+q*l]
    # deepcopy 인가가 더 빠르려나
    for i in range(N):
        for j in range(N):
            graph[i][j] = tmp[i][j]


# 솨ㅡ 흩뿌린다. 어떻게 표현을 못하겠네.
def graph_ungroup(l):
    # 손으로 써보면 복사도 필요 없고 연산 횟수 반으로 줄일 수 있음. 근데 구현을 못하겠다.
    tmp = [[0]*N for _ in range(N)]
    # N^4로 보이지만 N^2입니다. 아마.
    # 부분 배열 박스 그룹 개수
    for i in range(l):
        for j in range(l): 
            # 박스 내 수치
            for p in range(N//l):
                for q in range(N//l):
                    tmp[i+p*l][j+q*l] = graph[(N//l)*i+p][(N//l)*j+q]
                    
    # deepcopy 인가가 더 빠르려나
    for i in range(N):
        for j in range(N):
            graph[i][j] = tmp[i][j]

# 출력
for _ in range(R):
    # k: 연산 방식 , l: 부분 배열 크기 (2**l)
    k, l = map(int, input().split())
    l = 2**l

    # 모으고 흩뜨리는 연산이 필요
    if k >= 5:
        pass
        graph_group(l)
        l = N//l
        rotate(k-4, l)
        l = N//l
        graph_ungroup(l)        
    else:
        rotate(k, l)
        
for g in graph:
    print(*g)


'''
풀이 1 : 1차원 배열로 스왑하다가 2차원 배열로 할때보다 직관성만 떨어져서 리워크
풀이 2 : 21277 짠돌이 호석의 graph = list(zip(*graph[::-1])) 써먹어볼까 했는데 튜플 반환에 합치는 작업이 더 빡세서 포기
풀이 3 : 모으다 풀었다를 어떻게 설명해야될지를 모르겠다. 복습할 미래의 나가 엄청 똑똑하고 직관적이기를

다 풀고 너무 지쳐서 나중에 정리하는걸로...
안할거 아는데 비슷한 문제 나오면 하겠지
'''
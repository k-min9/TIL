'''
키워드 : 블록껍질, Convex hull 알고리즘, 그라함 스캔
설명 사이트 : https://johoonday.tistory.com/205
'''
import sys
input = sys.stdin.readline


# 기울기 구하기
def inclination(p1, p2):
    return p2[0] - p1[0], p2[1] - p1[1]
 
 # Counter Clock Wise : 예외가 되는 두 사항을 확인
def ccw(p1, p2, p3):
    v, u = inclination(p1, p2), inclination(p2, p3)
    if v[0] * u[1] > v[1] * u[0]:
        return True
    return False

# convex 알고리즘 (세점을 체크하여 180도 여부 확인)
def convex_hull(positions):
    convex = list()
    for p3 in positions:
        while len(convex) >= 2:
            p1, p2 = convex[-2], convex[-1]
            if ccw(p1, p2, p3):
                break
            convex.pop()
        convex.append(p3)
     
    return len(convex)


N, answer = int(input()), -2
positions = list()
for i in range(N):
    positions.append(list(map(int, input().split())))

# x축 y축 정렬
positions = sorted(positions, key=lambda pos:(pos[0], pos[1]))
answer += convex_hull(positions)

# 반대로 정렬 한번 더
positions.reverse()
answer += convex_hull(positions)
print(answer)

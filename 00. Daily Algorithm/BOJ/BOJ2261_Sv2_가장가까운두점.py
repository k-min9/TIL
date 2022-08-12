'''
~분할정복 Festival~ Final
수고하셨습니다 나!
'''
import sys
input = sys.stdin.readline


#두 점 사이의 거리
def distance(point1, point2): 
    return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2


def d_min(points):

    n = len(points)
    if n == 2 :  #점이 2개 일 때
        return distance(points[0],points[1])
    if n == 3 : # 점이 3개 일 때
        return min(distance(points[0],points[1]),distance(points[0],points[2]),distance(points[1],points[2]))

    # 반으로 나눠 x 좌표 기준 분할 정복
    d = min(d_min(points[:n//2]),d_min(points[n//2:]))
    
    check = [] # 후보 점
    for point in points: 
        # x거리가 d보다 짧은 거리에 있는 점들은 전부 후보
        if (points[n//2][0]-point[0])**2 < d: 
            check.append(point)

    # 세로로 기분 분할 정복하게 세팅
    check = sorted(check, key = lambda x : x[1])
    for i in range(len(check)-1): 
        for j in range(i+1,len(check)): 
            # y거리가 d보다 짧은 거리에 있는 점들은 전부 후보
            if (check[i][1]-check[j][1])**2 < d:
                d = min(d, distance(check[i],check[j])) 
            else: 
                break
    return d


num = int(input())
points = []

for i in range(num) : 
    x, y = map(int,input().split())
    points.append([x, y])
    
# x 좌표 기준 분할 정복하게 세팅
points = sorted(points, key = lambda x : x[0])
print(d_min(points))

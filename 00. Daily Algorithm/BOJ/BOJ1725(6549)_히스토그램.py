'''
from BOJ2571_색종이3.py 
비슷한 같은 꼴 문제
'''
# 1725번
import sys
input=sys.stdin.readline

n=int(input())
graph=[]
result=0
left=0
a=0
for _ in range(n):
    graph.append(int(input()))
graph.append(0)
stack=[(0,graph[0])]

for now in range(1,n+1):
    left=now
    while stack and stack[-1][1]>graph[now]:
        left,temp=stack.pop()
        result=max(result,temp*(now-left))
    stack.append((left,graph[now]))

print(result)

# 6549번
import sys
read=sys.stdin.readline

def maxSize():
    max_size = 0 #최대 넓이 저장
    stack = []

    for now in range(N):
        #왼쪽으로 이어질 수 있는 index
        left = now
        while stack and stack[-1][0] >= heights[now]:
            #pop되었다는 것은 추가 될 직사각형보다 높이가 높다는 의미이다.
            #따라서 추가될 직사각형은 pop되는 직사각형의 point값까지 넓어질 수 있다!
            #pop된 사각형의 point값으로 left를 업데이트
            h, left = stack.pop()
            tmp_size = h * (now-left)
            max_size = max(max_size, tmp_size)
        stack.append([heights[now],left])
    #탐색이 끝나고 아직 Stack에 남은 직사각형 정보로 maxSize 갱신(남았다는건 얘들이 제일 높이가 낮다는 뜻.)
    for h, point in stack:
        max_size = max(max_size, (N-point)*h)

    return max_size

while True:
    N, *heights = map(int,read().split())
    if N == 0: 
        break
    print(maxSize())
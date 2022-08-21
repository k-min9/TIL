'''
'나올 법'하면 풀어봐야지
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input())
positions = [list(map(int, input().split())) for _ in range(N)]
d = int(input())  # 철로 길이

# d보다 짧은 집들만 시작<끝점하게 만들고 끝 점 기준 재정렬
roads = []
for position in positions:
    house, office = position
    if abs(house - office) <= d:
        position = sorted(position)
        roads.append(position)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        # 힙 안에 존재하는 값이 끝 점 안에 있을 수 있는지 체크
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)

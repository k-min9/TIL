'''
접근 : N = 1500 > 삼각형 생각하면 완전탐색하면 1500C3 = 눈대중으로 5억.  
이거 O(N^2)으로 가능해아한다. > 각 점부터 점까지의 각도를 저장하면 되지 않나??
'''
import sys
input = sys.stdin.readline
from math import gcd

N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]

answer = 0
# 그래프 중에 하나를 기준점으로 잡는다. 이 점에서의 각도가 직각인지 체크할 것이다.
for origin in range(N):
    vectors = dict()
    for graph in graphs:
        if graphs[origin] == graph: continue
        # 기준점으로부터 각점간의 dx dy를 구해서 단위벡터(거의)화 하여 저장한다.
        # 이렇게 하면 기준점부터 해당점까지의 4분면 각을 저장한것과 다름 없다.
        x, y = graph
        dx = graphs[origin][0] - x
        dy = graphs[origin][1] - y
        d = gcd(dx, dy)
        dx /= d
        dy /= d
        if vectors.get((dx, dy)):
            vectors[(dx, dy)] += 1
        else:
            vectors[(dx, dy)] = 1

    # 저장된 점을 비교하여 기준점의 각이 직각인 삼각형이 총 몇개 인지 계산할 수 잇다.
    for x, y in vectors:
        next = vectors.get((-y, x))
        if next:
            answer += vectors[(-y, x)] * vectors[(x, y)]

# 출력
print(answer)

'''
기하학 난이도 무엇???
defaultdict 쓰니까 검색만 해도 value가 0인 내용물이 추가됨... 하나 배웠다...
'''
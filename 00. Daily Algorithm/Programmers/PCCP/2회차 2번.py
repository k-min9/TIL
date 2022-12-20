# 신입사원 교육
from heapq import heappop, heappush

def solution(ability, number):
    powers = list()
    
    for ab in ability:
        heappush(powers, ab)
    
    for _ in range(number):
        a = heappop(powers)
        b = heappop(powers)
        heappush(powers, a+b)
        heappush(powers, a+b)
    
    return sum(powers)

# 37
print(solution([10, 3, 7, 2], 2))

# 26
print(solution([1, 2, 3, 4], 3))
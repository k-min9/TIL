# https://leetcode.com/problems/gas-station
# 풀이 2 : 귀류법


def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    # 모든 주유소 방문 가능 여부 판별
    if sum(gas) < sum(cost):
        return -1
    
    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점이 안 되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
            
    return start

print(canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
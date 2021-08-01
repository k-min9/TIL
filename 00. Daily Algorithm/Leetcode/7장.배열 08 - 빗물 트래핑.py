# https://leetcode.com/problems/trapping-rain-water
# 풀이 1: 투포인터 풀이
# 풀이 1은 좁혀가며 전진, 풀이 2는 수위 높여가며 스택

def trap(self, height: list[int]) -> int:
    if not height:
        return 0
            
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)
        
        # 더 높은 쪽을 위해 투 포인터 이동 (핵심 비교 조건)   
        if left_max<=right_max: 
            volume = volume + (left_max - height[left])
            left = left + 1
        else:
            volume = volume + (right_max - height[right])
            right = right- 1
    return volume
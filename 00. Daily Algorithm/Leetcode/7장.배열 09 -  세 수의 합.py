# https://leetcode.com/problems/3sum
# 풀이 2: 투 포인터 풀이

def threeSum(self, nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        # 처음 제외, 중복값 건너 뛰기
        if i>0 and nums[i] == nums[i-1]:
            continue
        
        # 간격을 좁혀가며 계산
        left = i + 1
        right = len(nums) - 1
        
        while left<right:
            sum = nums[i] + nums[left] + nums[right]
            if sum <0:
                left += 1
            elif sum > 0:
                right -= 1
            else:  # 빙고
                result.append([nums[i], nums[left], nums[right]])
                
                # 스킵 처리
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -=1
                left += 1
                right -= 1
                
    return result    
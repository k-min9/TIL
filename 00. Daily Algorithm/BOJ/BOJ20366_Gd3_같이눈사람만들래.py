'''
네개 골라서 둘의 합 차이가 최소
투 포인터로 맞추기 
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 987654321

for i in range(N):
    for j in range(i + 3, N):  # i와 j 사이에 원소가 2개 이상 존재하게 됨
        left, right = i + 1, j - 1
        while left < right:
            tmp = (nums[i] + nums[j]) - (nums[left] + nums[right])
            if abs(ans) > abs(tmp):
                ans = abs(tmp)
            # 정렬이 되어 있기 때문에, tmp 가 0보다 작은 경우는(nums[left] + nums[right] > nums[i] + nums[j])
            # tmp 를 늘릴 필요가 있으므로 right 를 감소
            if tmp < 0: 
                right -= 1
            # 그 외, left 를 증가
            else: 
                left += 1

print(ans)

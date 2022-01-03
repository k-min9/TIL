'''
전위 순회 결과를 후위 순회로 변경
우선 전위의 맨 앞은 루트값이니까 -> 그 이후 자기보다 큰 값 나올때까지 루프+재귀 하는 식으로 찾으면 될 듯
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def solve(nums):
    length = len(nums)

    if length<=1:
        return nums

    for i in range(1, length):
        if nums[i] > nums[0]:
            return solve(nums[1:i]) + solve(nums[i:]) + [nums[0]]
    
    return solve(nums[1:]) + [nums[0]]


# 입력
nums = list()
while True:
    try:
        nums.append(int(input()))
    except:
        break

answers = solve(nums)
print(*answers)

'''
조합하는게 아니라 중간 중간 print 해주거나 인덱스를 사용하는 방법이 더 공간적으로도 좋았을 것같다.
'''


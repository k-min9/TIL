# https://leetcode.com/problems/product-of-array-except-self
# 풀이 1: 왼쪽에서 쭉 곱해 적고, 상황에 맞는 오른쪽을 곱해서 반환한다.


def productExceptSelf(self, nums: list[int]) -> list[int]:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p=1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례로 곱셈
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
        
    return out
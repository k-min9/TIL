'''
서로 다른 양의 정수 = 난이도 폭락 소리
N = 10만이면 NlogN 이하의 풀이를 쓰면 되는데 이건 걍 정렬 후 투포인터
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

left, right = 0, n-1
answer = 0
while left < right:
    sums = nums[left] + nums[right]
    if sums == x:
        answer += 1
        left += 1
    elif sums > x:
        right -= 1
    else:
        left += 1
print(answer)

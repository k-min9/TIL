'''
하나를 빼고 연속...?
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums_set = set(nums)


last_num = -1
cnt = 0
answer = 0
for num in nums_set:
    for n in nums:
        # 브루탈하게
        if n != num:
            if last_num != n:
                answer = max(answer, cnt)
                last_num = n
                cnt = 1
            else:
                cnt += 1
answer = max(answer, cnt)

print(answer)


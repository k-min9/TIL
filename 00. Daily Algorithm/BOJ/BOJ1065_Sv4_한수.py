'''
N 1000 이하 = 그냥 밀어라
가볍게 풀고 오늘은 코틀린코틀린
'''

N = int(input())

answer = 0
for i in range(1, N+1):
    nums = list(map(int, str(i)))
    if i < 100:
        answer += 1
    elif nums[0]-nums[1] == nums[1]-nums[2]:
        answer += 1

print(answer)

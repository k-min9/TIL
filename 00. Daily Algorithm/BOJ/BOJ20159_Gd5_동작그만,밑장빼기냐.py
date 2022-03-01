'''
좌에서의 합, 우에서의 합을 합쳐서 최대 값이 되는 시점이 답이네
'''
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sums_l = [0]
sums_r = [0]

for i in range(0,N,2):
    sums_l.append(sums_l[-1]+nums[i])

for i in range(N-1, 0, -2):
    sums_r.append(sums_r[-1]+nums[i])

answer = 0
for i in range(N//2 + 1):
    answer = max(answer, sums_l[i] + sums_r[N//2 - i])
# print(answer)

'''
평범히 틀림.
ㄴ아 밑장을 빼서 상대를 주는 경우?
'''

# 이대로 계산 강핼할 수 있으니 추가
answer2 = sums_l[-1]
for i in range(N-2, 1, -2):
    answer2 -= nums[i]
    answer2 += nums[i-1]
    answer = max(answer, answer2)

print(answer)

'''
계산 강행은 처음인것 같은데 평범하게 잘 되네 ㅎㅎ
리팩토링한다면 애초에 식이 깔끔히 안나오니 왔다갔다 세번 하는 식으로 했을 듯
'''

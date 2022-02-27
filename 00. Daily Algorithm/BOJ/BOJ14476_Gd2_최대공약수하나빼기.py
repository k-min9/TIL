'''
머리 좀 끙끙 써봤는데,
누적 GCD라고 불리는 웰노운 방식 중 하나라고 한다. 흐미...
왼쪽에서 부터 가는 lgcd와 오른쪽에서부터 오는 rgcd를 이용한 방식!
그 후 i를 제외하면, 남은 것은 1~i-1 / i+1~n-1
'''
import sys, math
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

lgcd = [0] * (N+1)  # out of range 때문에 하나 더 추가
rgcd = [0] * (N+1)  # 위와 동일

lgcd[0] = nums[0]
rgcd[N-1] = nums[N-1]
for i in range(1, N):
    lgcd[i] = math.gcd(lgcd[i-1], nums[i])
for i in range(N-2, -1, -1):
    rgcd[i] = math.gcd(rgcd[i+1], nums[i])

# 이 중 제일 큰 값을 가지고 약수 조건을 통과하면 정답...
answer = -1
answer2 = 0
for i in range(N):
    result = math.gcd(lgcd[i-1], rgcd[i+1])
    if nums[i] % result == 0:
        continue
    answer = max(answer, result)
    answer2 = nums[i]

if answer == -1:
    print(answer)
else:
    print(answer, answer2)

'''
또 하나 똑똑해져땅
'''
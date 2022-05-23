'''
쉬운 줄 알았는데... 어렵다?

풀이 : 스택의 제일 위의 값과 넣을 값을 비교하며 넣을 값이 클 경우 스택의 제일 위의 값을 제거합니다.
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().strip()))

result = []
delNum = K

for i in range(N):
    while delNum > 0 and result:
        if result[len(result)-1] < nums[i]:
            result.pop()
            delNum -= 1
        else:
            break
    result.append(nums[i])
    
for i in range(N-K):
    print(result[i],end="")

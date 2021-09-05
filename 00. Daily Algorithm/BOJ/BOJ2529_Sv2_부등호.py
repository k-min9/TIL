'''
접근 : 10! = 300만 남짓
초등학생들한테 뭔 짓을 시킨거냐
python에는 eval이 있습니다.
'''
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# N = int(input())
# exp = list(input().split())

# answer_min = "9999999999"
# answer_max = "0"
# for nums in permutations(range(10), N+1):
#     nums = ''.join(map(str,nums))
#     for i in range(N):
#         # 계속 true여야 함
#         if not eval(str(nums[i])+exp[i]+str(nums[i+1])):
#             break
#     else:
#         answer_max = max(answer_max, nums)
#         answer_min = min(answer_min, nums)
        

# print(answer_max)
# print(answer_min)

'''
네 시간 초과! 성실히 합시다 성실히! 어디서 느껴지는 데자뷰
'''

import sys
input = sys.stdin.readline

N = int(input())
exp = list(input().split())
chk = [0]*10
answer_max = ""
answer_min = "9999999999"

def dfs(cnt, answer):
    global answer_max, answer_min

    # 도달
    if cnt == N+1:
        answer_max = max(answer_max, answer)
        answer_min = min(answer_min, answer)
        return

    for i in range(10):
        if not chk[i]: 
            if cnt==0 or eval(answer[-1] + exp[cnt-1] + str(i)):
                chk[i] = 1
                dfs(cnt+1, answer + str(i)) 
                chk[i] = 0


dfs(0, "")
print(answer_max)
print(answer_min)

'''
연산자 끼워넣기3의 마이너 체인지 버전
'''
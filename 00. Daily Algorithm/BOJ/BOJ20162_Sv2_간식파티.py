'''
DP라...
'''

'''
풀이1 : 딱히 문제는 없음

import sys
input = sys.stdin.readline

N = int(input())

# 간식 모음
snacks = []

for _ in range(N):

    # 츄르가 영어로 뭐임???
    x = int(input())
    snacks.append([x,x])

    # 과자 합 갱신
    for i, snack in enumerate(snacks):
        if x > snack[0]:
            snacks[i] = [x, snack[1]+x]
    #print(snacks)

snacks.sort(key=lambda x:x[1])
print(snacks)
print(snacks[-1][1])
'''

'''
풀고보니 알겠다. 이거 RGB 거리 간식판이다. 
마지막 음식이 X 였을때의 최대합을 기록해두는게 아마 의도한 DP.
이러면 sort도 필요없고, 1차원 배열이면 끝남
'''

'''
풀이 2 : 개선판
'''

import sys
input = sys.stdin.readline

N = int(input())

# 이 간식을 마지막으로 먹었을때의 최대값
snacks = []
dp = []

for _ in range(N):

    # 뉴 간식
    x = int(input())

    # 새 간식을 마지막으로 먹었을때의 최대 값
    next_snack = x

    # 갱신
    for i, snack in enumerate(snacks):
        if snack < x :  # 더 맛있는 간식 = 최대 값 갱신
            next_snack = max(next_snack, x+dp[i])

    #다음으로
    snacks.append(x)
    dp.append(next_snack)

print(max(dp))

'''
생각한대로 딱딱 풀려주면 기부니가 조음
'''
'''
연속된 문자열, 최대 길이... 
난 일단  슬라이싱 윈도우가 떠올랐는데 DP라;;;
뭘 기록할지를 정해야 한다. >>> 같은 문자열이 나왔을때 묻는거다. 그 전에는 같았니???
'''

import sys
input = sys.stdin.readline

word_1 = input().rstrip()
word_2 = input().rstrip()

n = len(word_1)
m = len(word_2)
dp = [[0]*(m+1) for _ in range(n+1)]

answer = 0
for i in range(n):
    for j in range(m):
        if word_1[i] == word_2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
            answer = max(answer, dp[i+1][j+1])

print(answer)
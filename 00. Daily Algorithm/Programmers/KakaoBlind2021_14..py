from collections import Counter

# 0-1 배낭 문제
def solution(n, info):

     # 정보 정제
     info_score = list() # 점수 획득량
     info_need = list() # 점수획득을 위해 필요한 화살 수
     target = 0 # 아무것도 안할때 어피치 점수
     for i in range(11):
          if info[i] >= 1:
               info_score.append((10-i)*2)
               target += 10-i
          else:
               info_score.append((10-i))
          info_need.append(info[i]+1)

     # dp
     dp = [[0]*(n+1) for _ in range(11)]

     for i in range(1,11):
          for j in range(1, n+1):
               # 그 점수 버림
               if info_need[i-1] > j:
                    dp[i][j] = dp[i-1][j]          
               else:
                    # 그 점수 챙김
                    if info_score[i-1] + dp[i-1][j-info_need[i-1]] > dp[i-1][j]:
                         dp[i][j] = info_score[i-1] + dp[i-1][j-info_need[i-1]]
                    else:
                         dp[i][j] = dp[i-1][j]

     for d in dp:
          print(*d)

     # 역연산으로 리스트 구하기
     arrows = list()
     score = dp[10][n]
     w = n
     for i in range(10, 0, -1):
          if score <= 0:
               break
          if score == dp[i-1][w]:
               continue
          else:
               arrows.append(11 - i)
               score = score - info_score[i-1]
               w = w - info_need[i-1]

     answers = [0] * 10
     for arrow in arrows:
          answers[10-arrow] = info_need[10-arrow]
     answers.append(n - sum(answers))

     if dp[10][n] < target:
          return [-1]
     else:
          return answers

    

#print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
#print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
#print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))

# 일단 19개 통과
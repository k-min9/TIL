def solution(board, skill):
     R = len(board[0])
     C = len(board)
     answer = R*C

     for type, r1, c1, r2, c2, num in skill:
          if type == 1:
               num = -num
          for r in range(r1, r2+1):
               for c in range(c1, c2+1):
                    if -num >= board[r][c] > 0:
                         answer -= 1
                    elif num > -board[r][c] >=0:
                         answer += 1
                    board[r][c] += num       

     for b in board:
          print(*b)       

     return answer



print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6


'''
IMOS법이라고 한다.
'''
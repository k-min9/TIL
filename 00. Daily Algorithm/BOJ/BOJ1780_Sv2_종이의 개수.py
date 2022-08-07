'''
~분할정복 Festival~ 3/10
'''
import sys
input = sys.stdin.readline


# 정사각형 종이인지
def is_cube(x,y,size):
  global graphs

  # 첫 숫자와 하나라도 다르면 False
  num = graphs[x][y]
  for i in range(x,x+size):
    for j in range(y,y+size): 
      if graphs[i][j] != num:
        return False
  return True

# 9등분 하기
def divide_paper(x,y,size):
  global graphs
  global answers

  if is_cube(x,y,size):
    answers[graphs[x][y]+1] += 1
  else: 
    next_size = size//3
    for i in range(3): 
      for j in range(3): 
        divide_paper(x+next_size*i,y+next_size*j,next_size)


N = int(input())
graphs = [list(map(int, input().split())) for _ in range(N)]

# -1 0 1의 개수
answers = [0,0,0]

divide_paper(0,0,N)
print(answers[0])
print(answers[1])
print(answers[2])

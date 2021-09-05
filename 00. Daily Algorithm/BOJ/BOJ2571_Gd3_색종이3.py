'''
스터디 동료 풀이 코드 리뷰 + 블로그 참조
https://devlibrary00108.tistory.com/424
https://zoosso.tistory.com/155
베이스는 높이를 적어서 각 점당(O(N^2)) 가능한 사각형을 한번 쓱 긁어(O(N)) 구현하게 한 것 >> 최종 속도 O(N^3)
'''

import sys
input = sys.stdin.readline

paper = [[0]*102 for _ in range(100)]
for i in range(int(input())):
    x, y = map(int,input().split())
    for i in range(x+1,x+11):
        for j in range(y,y+10): 
            paper[j][i]=1

# 0행을 기준으로 높이값을 저장.(1이 이어지는 길이)
for i in range(1,100):
    for j in range(1,102):
        if paper[i][j]: 
            paper[i][j]=paper[i-1][j]+1

max_size = 0
# 행 순회
for row in range(100):
    paper_row = paper[row]
    # S는 계산하지 않은 열을 넣을 이전 열 idx stack 최초 값 0은 0열의 높이값은 모두 0이기 때문에 기준으로 삼기 위해.
    pre_idx_stack = [0]
    # 열 순회
    for cur_col in range(1,102):
        # S는 마지막으로 살펴본 열의 idx 현재 살펴보는열의 높이가 이전 열의 높이보다 작으면 같아질떄까지 s빼면서 직사각형 비교해줌.
        # 높이가 작아진다는 말은 곧 위에 빈칸이 있다는 뜻으로 빈칸이 반영 되기 이전에 높은 값에 대해 최대높이를 갱신시킨 후 넘어가겠다는 뜻.
        while pre_idx_stack and paper_row[pre_idx_stack[-1]] > paper_row[cur_col]:
            h = paper_row[pre_idx_stack[-1]]
            pre_idx_stack.pop()
            # cur_col-1는 현재 idx 바로 이전값 pre_idx_stack[-1]은 h높이를 가지는idx 
            max_size = max(max_size, (cur_col-pre_idx_stack[-1]-1)*h)
        pre_idx_stack.append(cur_col)
print(max_size)
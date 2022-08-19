'''
빗물 채우기 문제랑 엄청 유사한데 골드1?
키워드 : 스택
'''
import sys
input = sys.stdin.readline


nums = [int(input()) for _ in range(int(input()))]

stack = [] # (키, cnt)
result = 0

for num in nums:

  # 스택 끝 값보다 키 크면 pop하면서 cnt 정산
  while stack and stack[-1][0] < num:
    result += stack.pop()[1]

  # 스택이 비어있으면 해당 키 append하고 continue
  if not stack:
    stack.append((num, 1))
    continue
    
  # 스택 끝 값의 키와 같을 때
  if stack[-1][0] == num:
    cnt = stack.pop()[1]
    result += cnt

    if stack: 
        result += 1
    stack.append((num, cnt+1))

  # 스택 끝 값의 키보다 작을 때
  else:
    stack.append((num, 1))
    result += 1

# 결과값 출력
print(result)

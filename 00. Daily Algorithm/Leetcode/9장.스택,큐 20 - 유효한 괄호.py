# https://leetcode.com/problems/valid-parentheses
# 풀이 1: 매핑 테이블

def isValid(s: str) -> bool:
    stack = []
    table = {
                ')' : '(', 
                '}' : '{', 
                ']' : '[',
            }
    
    for char in s:
        # 없으면 집어넣고
        if char not in table:
            stack.append(char)
        # 있는데 그 값이 다음 값과 일치하지 않으면 바로 False
        elif not stack or table[char] != stack.pop():
            return False
        
    # 안 닫힌 괄호가 있으면 여기서 False
    return len(stack) == 0
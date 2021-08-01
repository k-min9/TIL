# https://leetcode.com/problems/remove-duplicate-letters
# 풀이 2: 스택에 set를 얹은 풀이(없는 것도 있음) 

import collections

def removeDuplicateLetters(s: str) -> str:
    counter = collections.Counter(s)
    seen = set()
    stack = []
    
    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        # 뒤에 그 문자가 남아 있고 그거 보다 사전식 배열이 빠르면 kill
        while(stack and char<stack[-1] and counter[stack[-1]]>0):  
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

        print('1',stack)
        
    return ''.join(stack)


print(removeDuplicateLetters('adbcvbd'))
# https://leetcode.com/problems/valid-palindrome/
# 풀이 3. 슬라이싱 사용

import re

def isPal(s: str): # 타입 표기
    s = s.lower()
    # 불필요 문자 필터링
    s = re.sub('[^a-z0-9]','',s)
    #return s

    return s == s[::-1]

#print(isPal('Mingming jump023'))
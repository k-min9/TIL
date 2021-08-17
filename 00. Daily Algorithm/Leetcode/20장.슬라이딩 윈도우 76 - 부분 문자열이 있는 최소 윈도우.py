# https://leetcode.com/problems/minimum-window-substring/
# 풀이 2 : 투 포인터 + 슬라이딩 윈도우

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        need = Counter(t)   # 필요한 t 수록
        missing = len(t)    # 이게 0이면 사이즈 조절
        start, end = 0, 0
        # 왼쪽 포인터
        i = 0

        for j, char in enumerate(s, 1):   # enumerate를 저렇게 쓰면 1부터 시작함
            # 오른쪽 포인터 이동하면서 확인 확인
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            # 네 0! 왼쪽 포인터의 이동을 판단한다.
            if missing == 0:  
                while i < j and need[s[i]] < 0:  #remove chars to find the real start
                    need[s[i]] += 1
                    i += 1
                # 다 끝나고 한번 더                    
                need[s[i]] += 1                  
                missing += 1   

                # 윈도우 업데이트
                if end == 0 or j-i < end-start:  
                    start, end = i, j
                i += 1  
        return s[start:end]

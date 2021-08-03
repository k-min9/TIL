# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 풀이 1: 슬라이딩 윈도우 + 투포인터

def lengthOfLongestSubstring(self, s: str) -> int:
    used = {}
    max_length = 0
    start = 0
    for idx, char in enumerate(s):
        # 등장 여부로 start 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, idx - start + 1)
            
        used[char] = idx
        
    return max_length
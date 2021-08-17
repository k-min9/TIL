# https://leetcode.com/problems/longest-repeating-character-replacement
# 풀이 1 : 투 포인터 + 카운터 + 슬라이딩 윈도우

import collections

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = collections.Counter()
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            # 가장 흔한 문자
            max_char_n = counts.most_common(1)[0][1]
            
            # k 초과시, 왼쪽 포인터 이동
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1
        # right이 1 커질때 left도 무조건 1 커지므로(한번커진 윈도우 사이즈는 불변) max연산은 필요 없다
        return right-left
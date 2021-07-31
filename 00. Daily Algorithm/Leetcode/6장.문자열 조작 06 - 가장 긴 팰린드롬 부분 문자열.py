# https://leetcode.com/problems/longest-palindromic-substring/
# 풀이 : 한칸씩 전진하면서 그 곳을 중심으로 확장체크(투 포인터)

def longestPalindrome(self, s: str) -> str:
    #팰린드롬 판별 및 투 포인터 확장
    def expand(left, right):
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    # 해당사항 없으면 빠르게 리턴
    if len(s)<2 or s == s[::-1]:
        return s
    
    # 시작 > 전진
    result = ''
    for i in range(len(s)-1):
        # key = len 새로운 비교방법!
        # 기존, 짝수 팰린드롬, 홀수 팰린드롬 중 가장 긴 것
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)
    return result
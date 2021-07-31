# https://leetcode.com/problems/most-common-word
# 풀이. 리스트 컴프리헨션 + Counter

import collections

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    
    counts = collections.Counter(words)
    # most_common으로 빈도수 가장 높은 것
    return counts.most_common(1)[0][0]
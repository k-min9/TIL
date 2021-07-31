# https://leetcode.com/problems/group-anagrams/
# 풀이 : 딕셔너리

import collections

def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
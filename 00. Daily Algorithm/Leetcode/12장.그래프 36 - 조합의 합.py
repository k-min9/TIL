# https://leetcode.com/problems/combination-sum
# 풀이 X: itertool은 중복조합도 지원합니다!

import itertools

def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
    comb_list = []
    candidates.sort()
    for i in range(1, target//candidates[0]+1):
        comb_list += list(map(list,itertools.combinations_with_replacement(candidates,i)))
            
    answer = []
    for c in comb_list:
        if sum(c) == target:
            answer.append(c)
            print(answer)
            
    return answer
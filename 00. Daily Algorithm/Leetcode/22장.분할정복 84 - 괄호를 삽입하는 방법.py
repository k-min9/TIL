# https://leetcode.com/problems/different-ways-to-add-parentheses
# 풀이  : 분할정복님 대단해요옷!

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l)+ op + str(r)))
            return results
    
        if expression.isdigit():
            return [int(expression)]
    
        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(compute(left, right, value))
        return results
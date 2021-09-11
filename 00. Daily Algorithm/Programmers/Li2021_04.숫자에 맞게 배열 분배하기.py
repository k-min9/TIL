'''
나눠라.
'''
def solution(n):

    def divide(answers, depth):
        # 혹시 몰라서
        if not answers:
            return None
        if len(answers) == 1:
            return answers

        num = nums[depth]
        ret = list()
        for i in range(num):
            ret += divide(answers[i::num], depth + 1)
        return ret
        
    # 소인수 분해
    nums = list()
    temp = n
    d = 2
    while temp != 1:
        if temp % d == 0:
            nums.append(d)
            temp = temp //d
        else:
            d += 1

    # 시작
    return divide(list(range(1,n+1)), 0)

print(solution(12)) 
print(solution(18)) 
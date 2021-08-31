def solution(dartResult):
    bonuses = {'S', 'D', 'T'}
    nums = list()
    for r in dartResult:
        if r.isdigit():
            if r == '0' and nums and nums[-1] == 1:
                nums.pop()
                nums.append(10)
            else:
                nums.append(int(r))
        elif r in bonuses:
            if r == 'D':
                nums[-1] = nums[-1] ** 2
            elif r == 'T':
                nums[-1] = nums[-1] ** 3
        else:
            if r == '*':
                n = min(len(nums), 2)
                for i in range(1,n+1):
                    nums[-i] *= 2
            else:
                nums[-1] *= -1
                
    answer = sum(nums)
    return answer

'''
문자열 조작 공부 조금 더 하긴 해야겠는데2
10 발라내는게 제일 힘들었다.
'''

# 아이디어 1 : 10을 k로 치환한다. 0점짜리 생각
# 아이디어 2 : idx 풀이: SDT를 만나서 그 앞에거를 죄다 변환해도 될것은 같음.
# 아이디어 3 : 숫자를 만나면 숫자를 넣고, 아닐 경우에는 0을 넣는 풀이
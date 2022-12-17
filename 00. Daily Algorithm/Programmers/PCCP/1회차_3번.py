# 유전형질
# N이 16 => dp시 4096만 = 하지마라
# 쿼리 5개 = 규칙찾아라
# 규칙 : 1 빼고 4진수로 바꿔서 앞에서 읽었을때 3이 나옴 rr / 0이 나옴 RR /그 외 = Rr

def checkParent(gen, num):
    num-=1
    ret = "Rr"
    while gen>1:
        if num%4 == 0:
            ret =  "RR"
        elif num%4 == 3:
            ret = "rr"
        num //= 4
        gen -= 1
    return ret

def solution(queries):
    answers = list()
    for gen, num in queries:
        answers.append(checkParent(gen, num))    
    return answers

# ["RR"]
print(solution([[3, 5]]))

# ["rr", "Rr"]
print(solution([[3, 8], [2, 2]]))

# ["RR", "Rr", "RR"]
print(solution([[3, 1], [2, 3], [3, 9]]))

# ["Rr"]
print(solution([[4, 26]]))

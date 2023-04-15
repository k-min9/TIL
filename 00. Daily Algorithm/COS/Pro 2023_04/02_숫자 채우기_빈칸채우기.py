'''
줄 채우기
COS 2중 배열 선언 방식 진짜 엄청 맘에 안듬
'''
answer = [[]]

def func_a(n):
    num = 1
    for i in range(n):
        for j in range(i+1):
            answer[i][j] += num
            num += 1

def func_b(n):
    num = 1
    for i in range(n):
        for j in range(n - i):
            answer[i][j] += num
            num += 1

def func_c(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if j >= n - i - 1:
                answer[i][j] += num
                num += 1

def func_d(n):
    num = 1
    for i in range(n):
        for j in range(n):
            if j >= i:
                answer[i][j] += num
                num += 1

def solution(n):
    global answer 
    answer = [[0 for col in range(n)] for row in range(n)]
    
    func_a(n)
    func_b(n)
    func_c(n)
    func_d(n)

    return answer
'''
일일히 매핑하고 체크하기를 함수화...
'''
board = [[0 for _ in range(100)] for _ in range(100)]

def func_a(param):
    ret = 0
    for i in range(0, 100):
        for j in range(0, 100):
            if board[i][j] == param:
                ret += 1
    return ret

def func_b():
    ret = 0
    for i in range(0, 100):
        for j in range(0, 100):
            ret = max(ret, board[i][j])
    return ret

def func_c(x, y):
    for i in range(x, x + 20):
        for j in range(y, y + 30):
            board[i][j] += 1
            
def solution(flyers):
    max_overlap = 0
    answer = 0
    for i in range(len(flyers)):
        func_c(flyers[i][0], flyers[i][1])
    max_overlap = func_b()
    answer = func_a(max_overlap)
    return answer
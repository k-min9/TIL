import sys
sys.stdin = open('input.txt')


# 가로 합
def calc1(row):
    return sum(boxes[row])


# 세로 합
def calc2(col):
    ret = 0
    for i in range(100):
        ret += boxes[i][col]
    return ret


# 대각선 1
def calc3():
    ret = 0
    for i in range(100):
        ret += boxes[i][i]
    return ret


# 대각선 2
def calc4():
    ret = 0
    for i in range(100):
        ret += boxes[i][99-i]
    return ret


for t in range(10):
    T = int(input())

    boxes = list()
    for i in range(100):
        boxes.append(list(map(int, input().split())))

    answer = 0
    for i in range(100):
        answer = max(answer, calc1(i))
        answer = max(answer, calc2(i))
    answer = max(answer, calc3())
    answer = max(answer, calc4())

    print(f'#{t+1}', answer)


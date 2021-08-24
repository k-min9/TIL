import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):

    N = int(input())
    boxes = [[0]*10 for _ in range(10)]

    answer = 0
    for i in range(N):
        xs, ys, xe, ye, color = map(int, input().split())
        for x in range(xs, xe+1):
            for y in range(ys, ye+1):
                # 이미 카운트 완료
                if boxes[x][y] == 101:
                    pass
                if boxes[x][y] == color or boxes[x][y] == 0:
                    boxes[x][y] = color
                else:
                    boxes[x][y] = 101
                    answer = answer + 1

    print(f'#{tc + 1}', answer)

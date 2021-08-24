import sys
sys.stdin = open('input.txt')


def is_valid(boxes):
    dic_row = [set() for _ in range(9)]
    dic_col = [set() for _ in range(9)]
    dic_box = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            # 소속 박스
            x = i//3
            y = j//3
            # 체크 대상
            chk = boxes[i][j]
            if chk in dic_row[i] or chk in dic_col[j] or chk in dic_box[x][y]:
                return 0
            else:
                dic_row[i].add(chk)
                dic_col[j].add(chk)
                dic_box[x][y].add(chk)
    return 1


T = int(input())
for t in range(T):
    boxes = list()
    for _ in range(9):
        boxes.append(list(map(str, input().split())))

    print(f'#{t+1}', is_valid(boxes))

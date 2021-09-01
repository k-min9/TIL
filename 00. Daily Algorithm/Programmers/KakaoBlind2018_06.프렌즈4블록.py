def solution(m, n, board):
    #0. 이거 안하면 문자 교체가 안됨
    board = [list(x) for x in board]
    
    answer = 0
    while True:
        # 1. 2*2 찾기
        target = set()
        for y in range(m-1):
            for x in range(n-1):
                if board[y][x] == board[y+1][x] == board[y][x+1] == board[y+1][x+1] and board[y][x] != '#':
                    target.add((y,x))
                    target.add((y+1,x)) 
                    target.add((y,x+1))
                    target.add((y+1,x+1))
                    
        # 2. 터뜨리고 대체하기 없으면 빠져나오기
        tmp = len(target)
        if tmp != 0:
            answer = answer + tmp
            for ty, tx in target:
                board[ty][tx] = '#'
        else:
            break
            
        # 3. 낙하운동 (#을 스왑으로 위로보낸다.)
        for x in range(n):
            for _ in range(m):
                for y in range(m-1):
                    if board[y+1][x] == '#':
                        board[y+1][x], board[y][x] = board[y][x], board[y+1][x]
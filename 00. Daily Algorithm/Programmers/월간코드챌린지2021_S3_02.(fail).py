# S는 0칸, L은 한칸, R은 3칸
moves = [(1,0), (0,1), (-1,0), (0,-1)]

def solution(grid):

    X = len(grid[0])
    Y = len(grid)
        
    answers = list()
    cnt = 0
    route = set()

    for x in range(X):
        for y in range(Y):
            for dir in range(4):
                fx, fy, fdir = x, y, dir
                while True:
                    dx, dy = moves[dir]
                    x = x + dx
                    y = y + dy
                    cnt = cnt + 1
                    if x>=X:
                        x = 0
                    if x<0:
                        x = X-1
                    if y>=Y:
                        y = 0
                    if y<0:
                        y = Y-1
                    if grid[y][x] == 'L':
                        dir = (dir + 1)%4
                    elif grid[y][x] == 'R':
                        dir = (dir + 3)%4
                    # 이미 확보한 사이클 여부
                    if (x,y,dir) in route:
                        cnt = 0
                        break
                    else:
                        route.add((x,y,dir))
                    
                    if x == fx and y == fy and dir == fdir:
                        answers.append(cnt) 
                        cnt = 0
                        break
    answers.sort()
    return answers

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))
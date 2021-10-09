'''
대각선 뒤집기
'''
from collections import defaultdict

def solution(grid, queries):
    for sy, sx, ey, ex, typ in queries:
        sy -= 1
        sx -= 1
        ey -= 1
        ex -= 1
    
    change_dic = defaultdict(list)
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            if typ == 1:
                change_dic[x+y].append((x, y))
            else:
                change_dic[x-y].append((x, y))

    for key, values in change_dic.items():
        values = sorted(values)
        n = len(values)
        for i in range(n//2):
            ax, ay = values[i]
            bx, by = values[-1-i]
            grid[ay][ax], grid[by][bx] = grid[by][bx], grid[ay][ax]

    return grid

grid = [[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18],[19,20,21,22,23,24,25,26,27],[28,29,30,31,32,33,34,35,36],[37,38,39,40,41,42,43,44,45]]
#print(solution(grid, [[1,2,5,7,1],[1,2,5,7,1]]))
print(solution(grid, [[1,1,2,2,1],[1,1,2,2,1]]))
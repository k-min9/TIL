MOVES = ((0,1), (0,-1), (1,0), (-1,0))

def solution(n, m, x, y, queries):
    now = {(x, y)}
    while queries:
        query, length = queries.pop()
        next = set()
        while now:
            nx, ny = now.pop()
            # 증식 아래로
            if query == 0 and ny == 0:
                for i in range(min(m, length +1)):
                    next.add((nx, i))
                continue
            # 증식 위로
            if query == 1 and ny == m-1:
                for i in range(min(m, length +1)):
                    next.add((nx, m-1-i))
                continue
            # 증식 오른쪽으로
            if query == 2 and nx == 0:
                for i in range(min(n, length +1)):
                    next.add((i, ny))
                continue
            # 증식 왼쪽으로
            if query == 3 and nx == n-1:
                for i in range(min(n, length +1)):
                    next.add((n-1-i, ny))
                continue
            # 그냥 이동
            dx = MOVES[query][0]*length
            dy = MOVES[query][1]*length
            nx += dx
            ny += dy
            nx = max(0, nx)
            nx = min(n-1, nx)
            ny = max(0, ny)
            ny = min(m-1, ny)
            next.add((nx, ny))
        now = next
    return len(now)

#print(solution(2, 2, 0, 0, [[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))

'''
역으로 이동해서 풀었는데 시간 초과(4/33) 나왔다. 논리는 정상인듯?
'''
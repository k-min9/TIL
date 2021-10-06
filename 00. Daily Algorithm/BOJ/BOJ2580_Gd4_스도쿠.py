import sys
input = sys.stdin.readline
from collections import defaultdict, deque


def dfs():
    if not visit:
        return True
    r, c = visit[0]
    t = (r // 3, c // 3)
    for next in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
        if next not in dic_rows[r] and next not in dic_cols[c] and next not in dic_boxes[t]:
            board[r][c] = next
            dic_rows[r].add(next)
            dic_cols[c].add(next)
            dic_boxes[t].add(next)
            visit.popleft()
            if dfs():
                return True
            else:
                board[r][c] = "."
                dic_rows[r].discard(next)
                dic_cols[c].discard(next)
                dic_boxes[t].discard(next)
                visit.appendleft((r, c))
    return False

board = [list(input().split()) for _ in range(9)]
dic_rows, dic_cols, dic_boxes, visit = defaultdict(set), defaultdict(set), defaultdict(set), deque([])
for r in range(9):
    for c in range(9):
        if board[r][c] != "0":
            dic_rows[r].add(board[r][c])
            dic_cols[c].add(board[r][c])
            dic_boxes[(r // 3, c // 3)].add(board[r][c])
        else:
            visit.append((r, c))

dfs()
for b in board:
    print(*b)
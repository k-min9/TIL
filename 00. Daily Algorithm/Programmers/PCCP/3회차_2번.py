MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def solution(image, fill):
    n = len(image)
    m = len(image[0])
    def coloring(r, c, color):
        r = r-1
        c = c-1
        visited = [[0]*m for _ in range(n)]
        visited[r][c] = 1
        color_init = image[r][c]
        image[r][c] = color

        queue = [[r, c]]
        while queue:
            r, c = queue.pop()
            for dx, dy in MOVES:
                nx = c + dx
                ny = r + dy
                if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and image[ny][nx] == color_init:
                    visited[ny][nx] = 1
                    image[ny][nx] = color
                    queue.append([ny, nx])

    for r, c, color in fill:
        coloring(r, c, color)

    return image
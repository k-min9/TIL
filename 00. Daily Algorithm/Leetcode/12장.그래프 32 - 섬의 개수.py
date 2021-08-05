# https://leetcode.com/problems/number-of-islands/
# 풀이 1: DFS 재귀.

def numIslands(self, grid: list[list[str]]) -> int:
    def dfs(i,j):
        #땅이 더 없을때까지 재귀
        if i < 0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != '1':
            return
        #물속에 집어넣어버리기~ > visited 안써도 됨
        grid[i][j] = 0
        
        # 동서남북 재귀
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  #새로운 육지 발견
                dfs(i,j)
                count = count + 1
    return count    
        
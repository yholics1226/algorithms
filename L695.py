# [Max Area of Island] https://leetcode.com/problems/max-area-of-island/

def maxAreaOfIsland(grid):
    n, m = len(grid), len(grid[0])
    def dfs(i, j):
        if 0 <= i < n and 0 <= j < m and grid[i][j]:
            grid[i][j] = 0
            return 1 + dfs(i-1, j) + dfs(i, j-1) + dfs(i, j+1) + dfs(i+1, j)
        return 0
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                ans = max(ans, dfs(i, j))
    return ans

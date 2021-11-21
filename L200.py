# [Number of Islands] https://leetcode.com/problems/number-of-islands/

def numIslands(grid):
    answer = 0
    n, m = len(grid), len(grid[0])
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    def DFS(x, y):
        grid[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                DFS(nx, ny)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                answer += 1
                print(i, j, answer)
                DFS(i, j)
    return answer

# [Shift 2D Grid] https://leetcode.com/problems/shift-2d-grid/

def shiftGrid(grid, k):
    m = len(grid)
    n = len(grid[0])
    answer = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            answer[((n*i+j+k)%(m*n))//n][((n*i+j+k)%(m*n))%n] = grid[i][j]
    return answer

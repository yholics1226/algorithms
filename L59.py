# [Spiral Matrix II] https://leetcode.com/problems/spiral-matrix-ii/

def generateMatrix(n):
    ans = [[0] * n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r, c, d, m = 0, -1, 0, 1
    while m <= n*n:
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and ans[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1) % 4
            continue
        ans[r][c] = m
        m += 1
    return ans

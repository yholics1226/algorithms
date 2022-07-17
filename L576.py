# [Out of Boundary Paths] https://leetcode.com/problems/out-of-boundary-paths/

from functools import lru_cache
def findPaths(m, n, maxMove, startRow, startColumn):
    @lru_cache(None)
    def cnt(move, row, col):
        if row < 0 or row == m or col < 0 or col == n:
            return 1
        if move == 0:
            return 0
        move -= 1
        return (cnt(move, row-1, col) + cnt(move, row, col-1) + cnt(move, row, col+1) + cnt(move, row+1, col)) % 1000000007
    return cnt(maxMove, startRow, startColumn)

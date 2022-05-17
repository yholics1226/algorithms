# [Shortest Path in Binary Matrix] https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque
def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] or grid[-1][-1]:
        return -1
    dx, dy = [-1, 0, 1, 1, 1, 0, -1, -1], [-1, -1, -1, 0, 1, 1, 1, 0]
    seen = set()
    q = deque([(0, 0, 1)])
    seen.add((0, 0))
    while q:
        x, y, d = q.popleft()
        if x == n-1 and y == n-1:
            return d
        for k in range(8): 
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen and not grid[nx][ny]:
                seen.add((nx, ny))
                q.append((nx, ny, d+1))
    return -1

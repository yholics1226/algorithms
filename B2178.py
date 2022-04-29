# [미로 탐색] https://www.acmicpc.net/problem/2178

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque([(0, 0)])
grid[0][0] = 2
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
            grid[nx][ny] = grid[x][y] + 1
            q.append((nx, ny))
print(grid[-1][-1] - 1)

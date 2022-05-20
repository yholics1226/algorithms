# [공주님을 구해라!] https://www.acmicpc.net/problem/17836

from collections import deque
import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
def sword():
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 0
                return i, j
sx, sy = sword()
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
grid[0][0] = 2
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
            grid[nx][ny] = grid[x][y] + 1
            q.append((nx, ny))
if grid[-1][-1]:
    ans = grid[-1][-1] - 2
    if grid[sx][sy]:
        ans = min(ans, grid[sx][sy] + n - sx + m - sy - 4)
elif grid[sx][sy]:
    ans = grid[sx][sy] + n - sx + m - sy - 4
else:
    ans = 100000
print(ans if ans <= t else 'Fail')

# another solution
from collections import deque
import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())
grid = [[*map(int, input().split())] for _ in range(n)]
sx, sy = -1, -1
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = 0
q = deque([(0, 0)])
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 1:
            if grid[nx][ny] == 2:
                sx, sy = nx, ny
            grid[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
ans = min(dist[-1][-1], dist[sx][sy] + n - sx + m - sy - 2)
print(ans if ans <= t else 'Fail')

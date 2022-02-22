# [유닛 이동시키기] https://www.acmicpc.net/problem/2194

import sys
from collections import deque
input = sys.stdin.readline
n, m, a, b, k = map(int, input().split())
grid = [[-1] * (m+1) for _ in range(n+1)]
for _ in range(k):
    x, y = map(int, input().split())
    grid[x][y] = -2
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
grid[sx][sy] = 0
Q = deque([(sx, sy)])
while Q:
    x, y = Q.popleft()
    if grid[ex][ey] > 0:
        break
    if x > 1 and grid[x-1][y] == -1:
        for k in range(b):
            if grid[x-1][y+k] == -2:
                break
        else:
            grid[x-1][y] = grid[x][y] + 1
            Q.append((x-1, y))
    if y > 1 and grid[x][y-1] == -1:
        for k in range(a):
            if grid[x+k][y-1] == -2:
                break
        else:
            grid[x][y-1] = grid[x][y] + 1
            Q.append((x, y-1))
    if x+a <= n and grid[x+1][y] == -1:
        for k in range(b):
            if grid[x+a][y+k] == -2:
                break
        else:
            grid[x+1][y] = grid[x][y] + 1
            Q.append((x+1, y))
    if y+b <= m and grid[x][y+1] == -1:
        for k in range(a):
            if grid[x+k][y+b] == -2:
                break
        else:
            grid[x][y+1] = grid[x][y] + 1
            Q.append((x, y+1))
print(grid[ex][ey])

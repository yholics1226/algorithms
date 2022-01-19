# [자리배정] https://www.acmicpc.net/problem/10157

import sys
input = sys.stdin.readline
c, r = map(int, input().split())
k = int(input())
if k > c * r:
    print(0)
    sys.exit(0)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d, x, y = 0, 0, 0
grid = [[0] * r for _ in range(c)]
grid[0][0] = 1
for _ in range(k-1):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < c and 0 <= ny < r and grid[nx][ny] == 0:
        x, y = nx, ny
    else:
        d = (d + 1) % 4
        x += dx[d]
        y += dy[d]
    grid[x][y] = 1
print(x+1, y+1)

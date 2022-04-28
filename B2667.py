# [단지번호붙이기] https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline
n = int(input())
grid = [[*map(int, list(input().rstrip()))] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = []
def dfs(x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny]:
            grid[nx][ny] = 0
            cnt[-1] += 1
            dfs(nx, ny)
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            grid[i][j] = 0
            cnt.append(1)
            dfs(i, j)
cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)

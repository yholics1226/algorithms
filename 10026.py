# [적록색약] https://www.acmicpc.net/problem/10026

# BFS
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(i, j):
    q = deque([(i, j)])
    seen[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
                if grid[nx][ny] == grid[x][y]:
                    seen[nx][ny] = True
                    q.append((nx, ny))
def cnt():
    c = 0
    for i in range(n):
        for j in range(n):
            if not seen[i][j]:
                dfs(i, j)
                c += 1
    return c
seen = [[False] * n for _ in range(n)]
print(cnt(), end=' ')
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'
seen = [[False] * n for _ in range(n)]
print(cnt())

# DFS (faster)
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(x, y):
    seen[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
            if grid[nx][ny] == grid[x][y]:
                dfs(nx, ny)
def cnt():
    c = 0
    for i in range(n):
        for j in range(n):
            if not seen[i][j]:
                dfs(i, j)
                c += 1
    return c
seen = [[False] * n for _ in range(n)]
print(cnt(), end=' ')
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R':
            grid[i][j] = 'G'
seen = [[False] * n for _ in range(n)]
print(cnt())

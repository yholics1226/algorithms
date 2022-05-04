# [안전 영역] https://www.acmicpc.net/problem/2468

from collections import deque
import sys, copy
input = sys.stdin.readline
n = int(input())
board = [[*map(int, input().split())] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 1
def bfs(i, j):
    q = deque([(i, j)])
    grid[i][j] = h
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > h:
                grid[nx][ny] = h
                q.append((nx, ny))
for h in range(1, max(map(max, board))):
    cnt = 0
    grid = copy.deepcopy(board)
    for x in range(n):
        for y in range(n):
            if grid[x][y] > h:
                cnt += 1
                bfs(x, y)
    ans = max(ans, cnt)
print(ans)

# not using deepcopy (faster)
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
grid = [[*map(int, input().split())] for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 1
def bfs(i, j, h):
    q = deque([(i, j)])
    ch[i][j] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > h and not ch[nx][ny]:
                ch[nx][ny] = True
                q.append((nx, ny))
for h in range(1, max(map(max, grid))):
    cnt = 0
    ch = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if grid[x][y] > h and not ch[x][y]:
                cnt += 1
                bfs(x, y, h)
    ans = max(ans, cnt)
print(ans)

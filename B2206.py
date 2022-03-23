# [벽 부수고 이동하기] https://www.acmicpc.net/problem/2206

# accepted in PyPy3, TLE in Python3
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
q = deque([(0, 0)])
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            if grid[nx][ny] == '0':
                q.append((nx, ny))
def bfs(wx, wy):
    q.append((wx, wy))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '0':
                if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and dist[i][j] != -1:
            bfs(i, j)
print(dist[-1][-1])

# accepted in Python3
from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
ch = [[[False] * m for _ in range(n)] for _ in range(2)]
ans = -1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
q = deque()
ch[0][0][0] = 1
q.append((0, 0, 1, 0))
while q:
    x, y, d, flag = q.popleft()
    if x == n-1 and y == m-1:
        ans = d
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and not ch[flag][nx][ny]:
            if grid[nx][ny] == '0':
                ch[flag][nx][ny] = 1
                q.append((nx, ny, d+1, flag))
            elif not flag:
                ch[1][nx][ny] = 1
                q.append((nx, ny, d+1, 1))
print(ans)

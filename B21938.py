# [영상처리] https://www.acmicpc.net/problem/21938

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
pxs = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

npxs = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        npxs[i][j] = int((pxs[i][3*j] + pxs[i][3*j+1] + pxs[i][3*j+2]) / 3 >= t) * 255

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

def BFS(i, j):
    Q = deque([(i, j)])
    npxs[i][j] = 0
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and npxs[nx][ny]:
                npxs[nx][ny] = 0
                Q.append((nx, ny))

cnt = 0
for i in range(n):
    for j in range(m):
        if npxs[i][j]:
            BFS(i, j)
            cnt += 1

print(cnt)

# [음식물 피하기] https://www.acmicpc.net/problem/1743

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
n, m, k = map(int, input().split())
fw = {tuple(map(int, input().split())) for _ in range(k)}
ans = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def DFS(x, y):
    global fw, cnt
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (nx, ny) in fw:
            fw -= {(nx, ny)}
            DFS(nx, ny)
            cnt += 1
    return cnt

for i in range(1, n+1):
    for j in range(1, m+1):
        if (i, j) in fw:
            fw -= {(i, j)}
            cnt = 1
            ans = max(ans, DFS(i, j))

print(ans)

# BFS
import sys
from collections import deque
input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0

def BFS(i, j):
    global ans
    Q = deque([(i, j)])
    cnt = 1
    while Q:
        x, y = Q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                graph[nx][ny] = 0
                Q.append((nx, ny))
                cnt += 1
    ans = max(ans, cnt)

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            graph[i][j] = 0
            BFS(i, j)

print(ans)

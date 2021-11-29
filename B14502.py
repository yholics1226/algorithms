# [연구소] https://www.acmicpc.net/problem/14502

import sys, copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
lst = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            lst.append(i * m + j)
com = list(combinations(lst, 3))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def count(board):
    Q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                Q.append([i, j])
    while Q:
        cur = Q.popleft()
        for i in range(4):
            nx = cur[0] + dx[i]
            ny = cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 2
                Q.append([nx, ny])
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1
    return cnt
def walls(board, nwall):
    for w in nwall:
        board[w // m][w % m] = 1
    return count(board)
ans = 0
for wall in com:
    ans = max(ans, walls(copy.deepcopy(lab), wall))
print(ans)

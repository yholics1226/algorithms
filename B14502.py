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

# w/o itertools - can be accepted in PyPy3, but time limit exceeded in Python3
import sys, copy
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
empty = 0
for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty += 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
cmin = float('inf')
def count(board):
    Q = deque()
    cnt = 0
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
                cnt += 1
                if cmin <= cnt:
                    return cmin
    return cnt
def walls(board, k):
    global ans, cmin
    if k == 0:
        cmin = count(copy.deepcopy(board))
    else:
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    board[i][j] = 1
                    walls(board, k-1)
                    board[i][j] = 0
walls(lab, 3)
print(empty - 3 - cmin)

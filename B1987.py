# [알파벳] https://www.acmicpc.net/problem/1987

import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
ans = 1
q = set([(0, 0, board[0][0])])
while q:
    x, y, path = q.pop()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in path:
            q.add((nx, ny, path + board[nx][ny]))
            ans = max(ans, len(path) + 1)
print(ans)

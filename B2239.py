# [스도쿠] https://www.acmicpc.net/problem/2239

import sys, copy
input = sys.stdin.readline
board = [list(input().rstrip()) for _ in range(9)]
r = [[False] * 10 for _ in range(10)]
c = [[False] * 10 for _ in range(10)]
g = [[False] * 10 for _ in range(10)]
z = []
for i in range(9):
    for j in range(9):
        if board[i][j] == '0':
            z.append([i, j])
        else:
            b = int(board[i][j])
            r[i][b] = c[j][b] = g[i // 3 * 3 + j // 3][b] = True
cnt = len(z)
flag = False
ans = []
def dfs(k):
    global flag, ans
    if flag:
        return
    if k == cnt:
        ans = copy.deepcopy(board)
        flag = True
        return
    else:
        xx, yy = z[k]
        gg = xx // 3 * 3 + yy // 3
        for i in range(1, 10):
            if not r[xx][i] and not c[yy][i] and not g[gg][i]:
                r[xx][i] = c[yy][i] = g[gg][i] = True
                board[xx][yy] = str(i)
                dfs(k+1)
                board[xx][yy] = '0'
                r[xx][i] = c[yy][i] = g[gg][i] = False
dfs(0)
for i in range(9):
    print(''.join(ans[i]))

# refactor
import sys
input = sys.stdin.readline
board = [[*map(int, list(input().rstrip()))] for _ in range(9)]
r = [[False] * 10 for _ in range(10)]
c = [[False] * 10 for _ in range(10)]
g = [[False] * 10 for _ in range(10)]
z = []
for i in range(9):
    for j in range(9):
        b = board[i][j]
        if not b:
            z.append([i, j])
        else:
            r[i][b] = c[j][b] = g[i // 3 * 3 + j // 3][b] = True
cnt = len(z)
ans = []
def dfs(k):
    if k == cnt:
        return True
    x, y = z[k]
    xx, yy, gg = r[x], c[y], g[x // 3 * 3 + y // 3]
    for i in range(1, 10):
        if not xx[i] and not yy[i] and not gg[i]:
            xx[i] = yy[i] = gg[i] = True
            board[x][y] = i
            if dfs(k+1):
                return True
            board[x][y] = 0
            xx[i] = yy[i] = gg[i] = False
    return False
dfs(0)
for i in range(9):
    print(''.join(map(str, board[i])))

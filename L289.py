# [Game of Life] https://leetcode.com/problems/game-of-life/

def gameOfLife(board):
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    for x in range(m):
        for y in range(n):
            cnt = 0
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] % 2:
                    cnt += 1
            if board[x][y]:
                if cnt < 2 or cnt > 3:
                    board[x][y] = 3
            elif cnt == 3:
                board[x][y] = 2
    for x in range(m):
        for y in range(n):
            if board[x][y] == 3:
                board[x][y] = 0
            elif board[x][y] == 2:
                board[x][y] = 1

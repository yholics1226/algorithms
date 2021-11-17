# [Minesweeper] https://leetcode.com/problems/minesweeper/

def updateBoard(board, click):
    m, n = len(board), len(board[0])
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]
    ch = [[0] * n for _ in range(m)]

    def DFS(pos):
        x, y = pos[0], pos[1]
        ch[x][y] = 1
        num = 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                num += 1
        if num == 0:
            board[x][y] = 'B'
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and ch[nx][ny] == 0:
                    DFS([nx, ny])
        else:
            board[pos[0]][pos[1]] = str(num)

    if board[click[0]][click[1]] == 'M':
        board[click[0]][click[1]] = 'X'
    else:
        DFS(click)

    return board

# [N-Queens] https://leetcode.com/problems/n-queens/

def solveNQueens(n):
    cols = [False] * n
    diag1 = [False] * (2*n-1)
    diag2 = [False] * (2*n-1)
    ans = []
    def dfs(k):
        if k == n:
            ans.append(list(board))
        for i in range(n):
            if not cols[i] and not diag1[i+k] and not diag2[i-k]:
                cols[i] = diag1[i+k] = diag2[i-k] = True
                board.append('.' * i + 'Q' + '.' * (n-i-1))
                dfs(k+1)
                board.pop()
                cols[i] = diag1[i+k] = diag2[i-k] = False
    board = []
    dfs(0)
    return ans

# another solution
def solveNQueens(n):
    cols = set()
    diag1 = set()
    diag2 = set()
    ans = []
    def dfs(k):
        if k == n:
            ans.append(list(board))
        for i in range(n):
            if i not in cols and i+k not in diag1 and i-k not in diag2:
                cols.add(i)
                diag1.add(i+k)
                diag2.add(i-k)
                board.append('.' * i + 'Q' + '.' * (n-i-1))
                dfs(k+1)
                board.pop()
                diag2.remove(i-k)
                diag1.remove(i+k)
                cols.remove(i)
    board = []
    dfs(0)
    return ans

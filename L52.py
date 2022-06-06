# [N-Queens II] https://leetcode.com/problems/n-queens-ii/

def totalNQueens(n):
    cols = [False] * n
    diag1 = [False] * (2*n-1)
    diag2 = [False] * (2*n-1)
    ans = 0
    def dfs(k):
        nonlocal ans
        if k == n:
            ans += 1
        else:
            for i in range(n if k else n//2):
                if not cols[i] and not diag1[k+i] and not diag2[k-i]:
                    cols[i] = diag1[k+i] = diag2[k-i] = True
                    dfs(k+1)
                    cols[i] = diag1[k+i] = diag2[k-i] = False
    dfs(0)
    ans *= 2
    if n % 2:
        m = n // 2
        cols[m] = diag1[m] = diag2[-m] = True
        dfs(1)
    return ans

# [The K Weakest Rows in a Matrix] https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

def kWeakestRows(mat, k):
    res = [(sum(mat[i]), i) for i in range(len(mat))]
    res.sort()
    return [res[i][1] for i in range(k)]

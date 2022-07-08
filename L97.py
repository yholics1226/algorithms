# [Interleaving String] https://leetcode.com/problems/interleaving-string/

def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    n, m = len(s1), len(s2)
    f = set()
    def dfs(i, j):
        if i == n and j == m:
            return True
        if (i, j) in f:
            return False
        if i < n and s1[i] == s3[i+j] and dfs(i+1, j):
            return True
        if j < m and s2[j] == s3[i+j] and dfs(i, j+1):
            return True
        f.add((i, j))
        return False
    return dfs(0, 0)

# memoization
from collections import defaultdict
def isInterleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False
    memo = defaultdict(lambda: -1)
    def dfs(i, j):
        if i == len(s1):
            return s3[i+j:] == s2[j:]
        if j == len(s2):
            return s3[i+j:] == s1[i:]
        if memo[(i, j)] != -1:
            return memo[(i, j)]
        memo[(i, j)] = ((s1[i] == s3[i+j]) and dfs(i+1, j)) or ((s2[j] == s3[i+j]) and dfs(i, j+1))
        return memo[(i, j)]
    return dfs(0, 0)

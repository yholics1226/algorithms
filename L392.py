# [Is Subsequence] https://leetcode.com/problems/is-subsequence/

def isSubsequence(s, t):
    n = len(s)
    i = 0
    for x in t:
        if i < n and x == s[i]:
            i += 1
    return i == n

# LCS using DP (slow)
def isSubsequence(s, t):
    n, m = len(s), len(t)
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[n][m] == n
